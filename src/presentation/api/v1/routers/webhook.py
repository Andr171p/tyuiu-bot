from fastapi import APIRouter, Request
from dishka.integrations.fastapi import FromDishka, DishkaRoute

from aiogram import Bot, Dispatcher
from aiogram.types import Update


webhook_router = APIRouter(
    tags=["Telegram webhooks"],
    route_class=DishkaRoute
)


@webhook_router.post(path="/webhook")
async def webhook(
        request: Request,
        bot: FromDishka[Bot],
        dp: FromDishka[Dispatcher]
) -> None:
    data = await request.json()
    update = Update.model_validate(data, context={"bot": bot})
    await dp.feed_update(
        bot=bot,
        update=update
    )
