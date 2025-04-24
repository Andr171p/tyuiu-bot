from datetime import datetime

from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command
from dishka.integrations.aiogram import FromDishka

from src.settings import Settings
from src.core.entities import User
from src.core.use_cases import UserManager


handler_router = Router()


@handler_router.message(Command("start"))
async def start(
        message: Message,
        user_manager: FromDishka[UserManager],
        settings: FromDishka[Settings]
) -> None:
    user = User(
        user_id=message.from_user.id,
        username=message.from_user.username,
        created_at=datetime.now()
    )
    await user_manager.register(user)
    await message.answer(settings.messages.start)


@handler_router.message(Command("info"))
async def info(message: Message, settings: FromDishka[Settings]) -> None:
    await message.answer(settings.messages.info)
