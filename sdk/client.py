#!/usr/bin/env python3
import redis, json, uuid, time, os

REDIS_HOST = os.getenv("REDIS_HOST", "localhost")
r = redis.Redis(host=REDIS_HOST, port=6379, decode_responses=True)
QUEUE = "beseri:tasks"

def push_task(ttype, payload, max_retries=3):
    task = {"id": str(uuid.uuid4()), "type": ttype, "payload": payload, "ts": time.time(), "retries": 0, "max_retries": max_retries}
    r.lpush(QUEUE, json.dumps(task))
    return task

if __name__ == "__main__":
    t = push_task("heavy_compute", {"n": 300}, max_retries=4)
    print("pushed", t)
