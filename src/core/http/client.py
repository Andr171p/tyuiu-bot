from src.core.http.base import BaseHTTP
from src.core.http.request import HTTPRequests


class HTTPClient(HTTPRequests, BaseHTTP):
    pass


import asyncio


async def main() -> None:
    text = "Как поступить в ТИУ"
    url = f"https://tyuiu-rag-production.up.railway.app/api/v1/rag/answer/?query={text}"
    async with HTTPClient() as client:
        resp = await client.get(url)
        print(resp)


asyncio.run(main())
