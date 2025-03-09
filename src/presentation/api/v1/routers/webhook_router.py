from fastapi import APIRouter, Request
from aiogram import Bot
from aiogram.types import Update

from dishka.integrations.fastapi import FromDishka

from src.presentation.bot.dp import dp


webhook_router = APIRouter()


@webhook_router.post(path="/webhook")
async def webhook(
        request: Request,
        bot: FromDishka[Bot],
) -> None:
    data = await request.json()
    update = Update.model_validate(data, context={"bot": bot})
    await dp.feed_update(
        bot=bot,
        update=update
    )
