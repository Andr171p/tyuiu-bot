import logging

from typing import Any, AsyncGenerator
from contextlib import asynccontextmanager

from aiogram import Bot
from fastapi import FastAPI

from src.ioc import container
from src.settings import Settings
from src.presentation.bot.app import dp
from src.presentation.bot.commands import set_commands
from src.infrastructure.broker.app import create_faststream_app


logger = logging.getLogger(__name__)


@asynccontextmanager
async def lifespan(app: FastAPI) -> AsyncGenerator[None, Any]:
    bot = await container.get(Bot)
    await set_commands(bot)
    logger.info("Bot set commands")
    settings = await container.get(Settings)
    webhook_url = f"{settings.app.url}/webhook"
    await bot.set_webhook(
        url=webhook_url,
        allowed_updates=dp.resolve_used_update_types(),
        drop_pending_updates=True
    )
    logger.info("Webhook set to: %s", webhook_url)

    faststream_app = await create_faststream_app()
    await faststream_app.broker.start()
    logger.info("Broker started")
    yield
    await faststream_app.broker.close()
    logger.info("Broker closed")

    await bot.delete_webhook()
    logger.info("Webhook removed")
