from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command

from src.services import AnalyticsService


start_router = Router()


@start_router.message(Command("start"))
async def start(message: Message) -> None:
    await AnalyticsService().register_user_by_message(message)
    await message.reply("Здарова заебал")
