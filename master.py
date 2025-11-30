#!/usr/bin/env python3
import redis
import json
import uuid
import time
import argparse
import os

REDIS_HOST = os.getenv("REDIS_HOST", "localhost")
REDIS_PORT = int(os.getenv("REDIS_PORT", 6379))
QUEUE = "beseri:tasks"

r = redis.Redis(host=REDIS_HOST, port=REDIS_PORT, decode_responses=True)

def make_task(tid, ttype, payload, max_retries=3):
    return {"id": tid, "type": ttype, "payload": payload, "ts": time.time(), "retries": 0, "max_retries": max_retries}

def produce(count=1, interval=0.5):
    for i in range(count):
        tid = str(uuid.uuid4())
        task = make_task(tid, "heavy_compute", {"n": 200 + i*10}, max_retries=4)
        r.lpush(QUEUE, json.dumps(task))
        print(f"[master] enqueued {task['id']} type={task['type']} payload={task['payload']}")
        time.sleep(interval)

if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--count", type=int, default=5)
    ap.add_argument("--interval", type=float, default=0.2)
    args = ap.parse_args()
    produce(count=args.count, interval=args.interval)
