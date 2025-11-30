#!/usr/bin/env python3
import os
import redis
import json
import time
import subprocess
import uuid
import psutil
import threading
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path

REDIS_HOST = os.getenv("REDIS_HOST", "localhost")
REDIS_PORT = int(os.getenv("REDIS_PORT", 6379))
QUEUE = "beseri:tasks"
PROCESSING = "beseri:processing"
RESULTS = "beseri:results"
DLQ = "beseri:dead"
META_PREFIX = "beseri:meta:"  # per-task metadata (popped_at)
VISIBILITY_TIMEOUT = 30  # seconds
MAX_WORKERS = int(os.getenv("MAX_WORKERS", "4"))
BACKOFF_BASE = 1.5

PLUGINS_DIR = Path("plugins/c_plugin")
r = redis.Redis(host=REDIS_HOST, port=REDIS_PORT, decode_responses=True)

def _move_to_processing():
    # Atomically move an item from QUEUE to PROCESSING and return it (or None)
    item = r.brpoplpush(QUEUE, PROCESSING, timeout=5)
    if item:
        try:
            task = json.loads(item)
            tid = task.get("id","")
            r.hset(META_PREFIX + tid, mapping={"popped_at": time.time()})
        except Exception:
            pass
    return item

def _remove_from_processing(raw):
    # remove one occurrence
    r.lrem(PROCESSING, 1, raw)
    try:
        task = json.loads(raw)
        tid = task.get("id","")
        r.delete(META_PREFIX + tid)
    except Exception:
        pass

def reaper_loop():
    # periodically scan processing list and requeue stale items
    while True:
        try:
            items = r.lrange(PROCESSING, 0, -1)
            now = time.time()
            for raw in items:
                try:
                    task = json.loads(raw)
                    tid = task.get("id","")
                    meta = r.hgetall(META_PREFIX + tid)
                    if not meta:
                        continue
                    popped_at = float(meta.get("popped_at", "0"))
                    if now - popped_at > VISIBILITY_TIMEOUT:
                        # move back to queue and remove from processing
                        print(f"[reaper] requeueing stale task {tid}")
                        r.lpush(QUEUE, raw)
                        _remove_from_processing(raw)
                except Exception:
                    continue
        except Exception as e:
            print("[reaper] exception", e)
        time.sleep(5)

def call_c_plugin(n):
    bin_path = PLUGINS_DIR / "bin" / "heavy_compute"
    if not bin_path.exists():
        return {"error": "plugin_missing"}
    start = time.time()
    proc = subprocess.run([str(bin_path), str(n)], capture_output=True, text=True)
    duration = time.time() - start
    out = proc.stdout.strip()
    return {"retcode": proc.returncode, "output": out, "duration": duration}

def process_task_raw(raw):
    try:
        task = json.loads(raw)
    except Exception:
        return None, {"error": "invalid_json"}
    ttype = task.get("type")
    if ttype == "heavy_compute":
        n = int(task.get("payload", {}).get("n", 200))
        res = call_c_plugin(n)
        return task.get("id"), res
    else:
        return task.get("id"), {"retcode": 0, "output": "noop", "duration": 0}

def worker_loop():
    print("[worker] started")
    with ThreadPoolExecutor(max_workers=MAX_WORKERS) as ex:
        futures = set()
        while True:
            # submit new tasks up to capacity
            try:
                while len(futures) < MAX_WORKERS:
                    raw = _move_to_processing()
                    if not raw:
                        break
                    future = ex.submit(process_task_raw, raw)
                    # attach raw to future for cleanup
                    future.raw = raw
                    futures.add(future)
            except Exception as e:
                print("[worker] fetch exception", e)

            done, _ = as_completed(futures, timeout=1), None
            # gather completed
            to_remove = set()
            for fut in list(futures):
                if fut.done():
                    tid, result = None, None
                    try:
                        tid, result = fut.result()
                    except Exception as e:
                        print("[worker] task exception", e)
                        # treat as failure
                        tid = None
                        result = {"retcode": 2, "output": "exception"}
                    raw = getattr(fut, "raw", None)
                    # finished, handle result
                    if result.get("retcode", 0) == 0:
                        # success
                        print(f"[worker] task {tid} success")
                        # push result and cleanup
                        payload = {"task_id": tid, "result": result, "ts": time.time()}
                        r.lpush(RESULTS, json.dumps(payload))
                        if raw:
                            _remove_from_processing(raw)
                    else:
                        # failure handling: retries
                        try:
                            task = json.loads(raw)
                            retries = int(task.get("retries", 0)) + 1
                            task["retries"] = retries
                            maxr = int(task.get("max_retries", 3))
                            if retries > maxr:
                                print(f"[worker] task {task.get('id')} -> dead (retries={retries})")
                            r.lpush(DLQ, json.dumps(task))
                            if raw:
                                _remove_from_processing(raw)
                            else:
                                backoff = BACKOFF_BASE ** retries
                                print(f"[worker] retrying {task.get('id')} in {backoff:.1f}s (attempt {retries}/{maxr})")
                                time.sleep(min(backoff, 10))
                                r.lpush(QUEUE, json.dumps(task))
                                if raw:
                                    _remove_from_processing(raw)
                        except Exception as e:
                            print("[worker] failure handling exception", e)
                            if raw:
                                _remove_from_processing(raw)
                    to_remove.add(fut)
            # remove done futures
            for fut in to_remove:
                futures.discard(fut)
            time.sleep(0.1)

if __name__ == "__main__":
    # start reaper thread
    t = threading.Thread(target=reaper_loop, daemon=True)
    t.start()
    worker_loop()
