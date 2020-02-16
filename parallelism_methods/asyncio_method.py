from funcs_for_test import make_3_dim_list
import asyncio
import time
from memory_profiler import memory_usage

mem = memory_usage(-1, interval=.2, timeout=1)
n = 200
t = 8

import asyncio

async def nested(count, add):
    lst = []
    start = time.monotonic()
    for i in range(count):
        for j in range(count):
            for g in range(count):
                lst.append([i, j, g])
    print(time.monotonic() - start, add)

async def main():
    # Schedule nested() to run soon concurrently
    # with "main()".
    tasks = [asyncio.create_task(nested(n, i)) for i in range(t)]

    # "task" can now be used to cancel "nested()", or
    # can simply be awaited to wait until it is complete:
    for task in tasks:
        await task

asyncio.run(main())

print(mem)
