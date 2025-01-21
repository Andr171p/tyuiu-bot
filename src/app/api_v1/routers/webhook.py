from fastapi import APIRouter, Request
from aiogram.types import Update

from src.app.bot import bot, dp


wh_router = APIRouter()


@wh_router.post(path="/webhook")
async def webhook(request: Request) -> None:
    data = await request.json()
    update = Update.model_validate(data, context={"bot": bot})
    await dp.feed_update(
        bot=bot,
        update=update
    )
