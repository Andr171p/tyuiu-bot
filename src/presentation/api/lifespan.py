import logging
from contextlib import (
    asynccontextmanager,
    AbstractAsyncContextManager
)

from fastapi import FastAPI
from aiogram import Bot

from src.di import container
from src.presentation.bot.app import dp
from src.settings import settings


log = logging.getLogger(__name__)


@asynccontextmanager
async def lifespan(app: FastAPI) -> AbstractAsyncContextManager[None]:
    bot = await container.get(Bot)
    webhook_url: str = f"{settings.api.url}/webhook"
    await bot.set_webhook(
        url=webhook_url,
        allowed_updates=dp.resolve_used_update_types(),
        drop_pending_updates=True
    )
    log.info("Webhook set to: %s", webhook_url)
    yield
    await bot.delete_webhook()
    log.info("Webhook removed")
