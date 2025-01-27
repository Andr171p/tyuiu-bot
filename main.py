'''import logging
import asyncio

from src.app.bot.run import run_chat_bot


async def main() -> None:
    logging.basicConfig(level=logging.INFO)
    await run_chat_bot()


if __name__ == "__main__":
    asyncio.run(main())'''

import asyncio
import aiohttp


async def main() -> None:
    url = "https://tyuiu-rag-bot-production.up.railway.app/api/v1/notifications/sendAll/"
    async with aiohttp.ClientSession() as session:
        async with session.post(
            url=url,
            json={
                "text": "kcjsdjvibni"
            }
        ) as response:
            print(await response.json())


asyncio.run(main())