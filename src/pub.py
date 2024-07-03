import random
import time
from uuid import uuid4

from sync import client

if __name__ == "__main__":
    while True:
        num = random.random()
        id = uuid4()
        client.publish("channel", f"{id}: Hello, World! {num}")
        print(f"{id}: Hello, World! {num}")
        time.sleep(num)
