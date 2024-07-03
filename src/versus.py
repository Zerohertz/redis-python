import asyncio
from collections import defaultdict

import zerohertzLib as zz

from asyn import main as main_async
from sync import main as main_sync

if __name__ == "__main__":
    rng = range(10, 1000, 50)
    data = defaultdict(list)
    for i in rng:
        data["Sync"].append(main_sync(i))
        data["Async"].append(asyncio.run(main_async(i)))
    zz.plot.plot(
        list(rng),
        data,
        xlab="Number of Requests",
        ylab="Processing Time [sec]",
        title="Sync vs. Async",
    )
