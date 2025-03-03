from datetime import datetime

from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command

from dishka.integrations.aiogram import FromDishka

from src.schemas import UserSchema
from src.services import UserService
from src.misc.files_readers import load_txt_async
from src.config import settings


start_router = Router()


@start_router.message(Command("start"))
async def start(
        message: Message,
        user_service: FromDishka[UserService]
) -> None:
    user = UserSchema.from_message(message)
    await user_service.register(user)
    file_path = settings.static.texts_dir / "Start_message.txt"
    text = await load_txt_async(file_path)
    await message.answer(text)
