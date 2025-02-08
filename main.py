"""
import logging
import asyncio

from src.app.bot.run import run_chat_bot


async def main() -> None:
    logging.basicConfig(level=logging.INFO)
    await run_chat_bot()


if __name__ == "__main__":
    asyncio.run(main())
"""

'''import asyncio
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


asyncio.run(main())'''

'''import asyncio
from src.apis import ChatAPI
from src.schemas import QuestionSchema


async def main() -> None:
    chat_api = ChatAPI()
    question = QuestionSchema(
        question="Поступлю ли я на архитектуру с суммой баллов 278"
        )
    ans = await chat_api.answer_on_question(question)
    print(ans)


asyncio.run(main())'''


import asyncio
from src.repository import MessageRepository
from src.utils.metrics import get_count_per_day


async def main() -> None:
    result = await get_count_per_day(MessageRepository())
    print(result)
    
    
asyncio.run(main())