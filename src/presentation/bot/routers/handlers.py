from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command
from dishka.integrations.aiogram import FromDishka

from src.settings import Settings
from src.core.services import UserService


handler_router = Router()


@handler_router.message(Command("start"))
async def start(
        message: Message,
        user_service: FromDishka[UserService],
        settings: FromDishka[Settings]
) -> None:
    await user_service.save(message.from_user.id, message.from_user.username)
    await message.answer(settings.messages.start)


@handler_router.message(Command("info"))
async def info(message: Message, settings: FromDishka[Settings]) -> None:
    await message.answer(settings.messages.info)
