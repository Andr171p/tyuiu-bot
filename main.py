import logging
import asyncio

from src.app.run import run_chat_bot


async def main() -> None:
    logging.basicConfig(level=logging.INFO)
    await run_chat_bot()


if __name__ == "__main__":
    asyncio.run(main())
