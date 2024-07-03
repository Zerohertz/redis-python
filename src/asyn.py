import asyncio
import os
import time
from uuid import uuid4

import redis.asyncio as redis

HOST = os.getenv("REDIS_HOST", "redis")
PORT = int(os.getenv("REDIS_PORT", 6379))
DB = int(os.getenv("REDIS_DB", 0))

client = redis.Redis(host=HOST, port=PORT, db=DB)


async def _set(key, value):
    await client.set(key, value)
    await asyncio.sleep(0.01)


async def _get(key):
    value = await client.get(key)
    await asyncio.sleep(0.01)
    return value


async def main(nums):
    try:
        await client.ping()
        print("Connected to Redis (Async)")
    except redis.ConnectionError:
        print("Could not connect to Redis (Async)")
    start_time = time.time()
    ids = [uuid4() for _ in range(nums)]
    await asyncio.gather(*(_set(f"key-{id}", f"value-{id}") for id in ids))
    await asyncio.gather(*(_get(f"key-{id}") for id in ids))
    end_time = time.time()
    print(f"Async: {end_time - start_time:.2f} seconds")
    await client.aclose()
    return end_time - start_time


if __name__ == "__main__":
    asyncio.run(main(1000))
