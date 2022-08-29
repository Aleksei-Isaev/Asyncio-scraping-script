import asyncio
import time

from bs4 import BeautifulSoup
from httpx import AsyncClient

URL = "https://djinni.co/jobs/keyword-python/"


async def get_djinni_jobs(page: int, client: AsyncClient):
    response = await client.get(URL, params={"page": page})  # API request
    soup = BeautifulSoup(response.content, "html.parser")
    return [job.text.strip() for job in soup.select(".profile")]


async def main():
    async with AsyncClient() as client:
        jobs_pages = await asyncio.gather(*[get_djinni_jobs(page, client) for page in range(5, 15)])

        for jobs in jobs_pages:
            print(jobs)


if __name__ == "__main__":
    start_time = time.perf_counter()
    asyncio.run(main())
    end_time = time.perf_counter()
    print("Elapsed:", end_time - start_time)
