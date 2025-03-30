import asyncio
import aiohttp
import time
from typing import List, Dict
import statistics

class LoadTester:
    def __init__(self, url: str, concurrency: int = 10, duration: int = 30):
        self.url = url
        self.concurrency = concurrency
        self.duration = duration
        self.results: List[float] = []

    async def make_request(self):
        async with aiohttp.ClientSession() as session:
            start_time = time.time()
            async with session.get(self.url) as response:
                await response.text()
                end_time = time.time()
                self.results.append(end_time - start_time)

    async def run_load_test(self):
        tasks = []
        start_time = time.time()
        
        while time.time() - start_time < self.duration:
            tasks.extend([self.make_request() for _ in range(self.concurrency)])
            await asyncio.gather(*tasks)
            tasks = []

    def get_statistics(self) -> Dict:
        return {
            "total_requests": len(self.results),
            "avg_response_time": statistics.mean(self.results),
            "min_response_time": min(self.results),
            "max_response_time": max(self.results),
            "requests_per_second": len(self.results) / self.duration
        }
