import logging
from contextlib import (
    asynccontextmanager,
    AbstractAsyncContextManager
)

from fastapi import FastAPI

from src.app.bot import bot, dp
from src.config import settings


log = logging.getLogger(__name__)


@asynccontextmanager
async def lifespan(app: FastAPI) -> AbstractAsyncContextManager[None]:
    wh_url: str = f"{settings.app.url}/webhook"
    await bot.set_webhook(
        url=wh_url,
        allowed_updates=dp.resolve_used_update_types(),
        drop_pending_updates=True
    )
    log.info("Webhook set to: %s", wh_url)
    yield
    await bot.delete_webhook()
    log.info("Webhook removed")
