from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command

from src.presentation.bot.presenters import InfoPresenter


info_router = Router()


@info_router.message(Command("info"))
async def info(message: Message) -> None:
    await InfoPresenter.present(message)
