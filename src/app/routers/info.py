from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command

from src.misc.file_loaders import load_txt_async
from src.config import settings


info_router = Router()


@info_router.message(Command("info"))
async def info(message: Message) -> None:
    file_path = settings.static.texts_dir / "info.txt"
    text = await load_txt_async(file_path)
    await message.answer(text)
