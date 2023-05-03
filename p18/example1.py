import time
import numpy as np
import asyncio
import aiohttp

from time import sleep
import requests
from concurrent.futures import ThreadPoolExecutor
from threading import get_ident


workers = 10
sleepy_times = np.random.randint(2, 7, workers)

def request_get(url):
    return requests.get(url)

def parallel(task_id):
    start = time.time()

    sleep_time = sleepy_times[task_id]

    pid = get_ident()
    print(f"Fetch parallel process {pid}/({task_id}) started, sleeping for {sleep_time} seconds")

    sleep(sleep_time)

    # response = request_get('https://api.github.com/events')
    # datetime = response.headers.get('Date')
    # response.close()

    elapsed = time.time() - start
    return f"Process {pid}: {1}, took: {elapsed:.2f} seconds"


def main():
    pool = ThreadPoolExecutor(workers)

    start = time.time()

    res = list(pool.map(parallel, range(workers)))
    print(*res, sep='\n')

    elapsed = time.time() - start
    print(f"Process took: {elapsed}s")

main()






async def aiohttp_get(url):
    # https://docs.aiohttp.org/en/stable/client_quickstart.html
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            return response

async def async_function(pid):
    start = time.time()

    sleep_time = sleepy_times[pid]

    print(f"Fetch async process {pid} started, sleeping for {sleep_time} seconds")

    await asyncio.sleep(sleep_time)

    # response = await aiohttp_get('https://api.github.com/events')
    # datetime = response.headers.get('Date')
    # response.close()

    elapsed = time.time() - start
    return f"Process {pid}: {1}, took: {elapsed:.2f} seconds"


async def main():
    start = time.time()

    aaa = map(async_function, range(workers))
    for i, task in enumerate(asyncio.as_completed(aaa)):
        result = await task
        print(">>" * (i + 1), result)

    elapsed = time.time() - start
    print(f"Process took: {elapsed}s")


asyncio.run(main())