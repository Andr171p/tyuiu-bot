from fastapi import APIRouter, Request
from aiogram import Bot, Dispatcher
from aiogram.types import Update

from dishka.integrations.fastapi import FromDishka


wh_router = APIRouter()


@wh_router.post(path="/webhook")
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
