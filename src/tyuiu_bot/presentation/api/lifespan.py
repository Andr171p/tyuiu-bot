from typing import Any, AsyncGenerator
from contextlib import asynccontextmanager

import logging

from aiogram import Bot
from fastapi import FastAPI

from ..bot.app import dp
from ..bot.commands import set_commands

from ...ioc import container
from ...settings import Settings
from ...infrastructure.broker.app import create_faststream_app


logger = logging.getLogger(__name__)


@asynccontextmanager
async def lifespan(app: FastAPI) -> AsyncGenerator[None, Any]:
    bot = await container.get(Bot)
    await set_commands(bot)
    logger.info("Bot set commands")

    faststream_app = await create_faststream_app()
    await faststream_app.broker.start()
    logger.info("Broker started")

    settings = await container.get(Settings)
    webhook_url = settings.bot.WEBHOOK_URL
    await bot.set_webhook(
        url=webhook_url,
        allowed_updates=dp.resolve_used_update_types(),
        drop_pending_updates=True
    )
    logger.info("Webhook set to: %s", webhook_url)

    yield

    await faststream_app.broker.close()
    logger.info("Broker closed")

    await bot.delete_webhook()
    logger.info("Webhook removed")
