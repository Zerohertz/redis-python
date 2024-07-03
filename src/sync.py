import os
import time
from uuid import uuid4

import redis

HOST = os.getenv("REDIS_HOST", "redis")
PORT = int(os.getenv("REDIS_PORT", 6379))
DB = int(os.getenv("REDIS_DB", 0))

client = redis.Redis(host=HOST, port=PORT, db=DB)


def main(nums):
    try:
        client.ping()
        print("Connected to Redis (Sync)")
    except redis.ConnectionError:
        print("Could not connect to Redis (Sync)")
    start_time = time.time()
    ids = [uuid4() for _ in range(nums)]
    for id in ids:
        client.set(f"key-{id}", f"value-{id}")
        time.sleep(0.01)
    for id in ids:
        value = client.get(f"key-{id}")
        time.sleep(0.01)
    end_time = time.time()
    print(f"Sync: {end_time - start_time:.2f} seconds")
    return end_time - start_time


if __name__ == "__main__":
    main(1000)
