import time

import httpx
import asyncio

URL = "http://127.0.0.1:8000/polls/"


async def fetch(url, client, semaphore):
    async with semaphore:
        start = time.time()
        try:
            response = await client.get(url)
            return response.status_code == 200, time.time() - start
        except:
            return False, time.time() - start


async def make_requests(url, n, c):
    semaphore = asyncio.Semaphore(c)
    async with httpx.AsyncClient(limits=httpx.Limits(max_connections=c), timeout=10) as client:
        tasks = [fetch(url, client, semaphore) for _ in range(n)]
        return await asyncio.gather(*tasks)


result = asyncio.run(make_requests(URL, 180, 20))
print("num of requests:", len(result))
print("num of error:", len([d for f, d in result if not f]))
durations = sorted(d * 1000 for f, d in result)
hist = [0, 20, 50, 100, 200, 500, 1000, 2000, 5000, 10000]
for f, t in zip(hist, hist[1:]):
    print(f"num duration from {f}ms to {t}ms:", len([d for d in durations if f <= d < t]))
    if t == 10000:
        print(f"num duration more {t}ms:", len([d for d in durations if t <= d]))
