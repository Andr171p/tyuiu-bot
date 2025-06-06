from fastapi import APIRouter, Request

from aiogram import Bot
from aiogram.types import Update

from dishka.integrations.fastapi import FromDishka, DishkaRoute

from src.tyuiu_bot.presentation.bot.app import dp


webhook_router = APIRouter(
    tags=["Telegram webhooks"],
    route_class=DishkaRoute
)


@webhook_router.post(path="/webhook")
async def webhook(request: Request, bot: FromDishka[Bot]) -> None:
    data = await request.json()
    update = Update.model_validate(data, context={"bot": bot})
    await dp.feed_update(bot=bot, update=update)
