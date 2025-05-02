from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command
from dishka.integrations.aiogram import FromDishka

from src.settings import Settings


handler_router = Router()


@handler_router.message(Command("start"))
async def start(message: Message, settings: FromDishka[Settings]) -> None:
    await message.answer(settings.messages.start)


@handler_router.message(Command("info"))
async def info(message: Message, settings: FromDishka[Settings]) -> None:
    await message.answer(settings.messages.info)
