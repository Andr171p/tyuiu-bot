from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command

from dishka.integrations.aiogram import FromDishka

from src.services import AnalyticsService
from src.misc.file_loaders import load_txt_async
from src.config import settings


start_router = Router()


@start_router.message(Command("start"))
async def start(
        message: Message,
        analytics_service: FromDishka[AnalyticsService]
) -> None:
    await analytics_service.register_user_by_message(message)
    file_path = settings.static.texts_dir / "start.txt"
    text = await load_txt_async(file_path)
    await message.answer(text)
