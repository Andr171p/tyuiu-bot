from src.http.base import BaseHTTP
from src.http.request import HTTPRequests


class HTTPClient(HTTPRequests, BaseHTTP):
    pass


import asyncio


async def main() -> None:
    text = "Как поступить в ТИУ"
    url = f"https://tyuiu-rag-api-production.up.railway.app/api/v1/chat/answer/?query={text}"
    async with HTTPClient() as client:
        resp = await client.get(url)
        print(resp)


asyncio.run(main())
