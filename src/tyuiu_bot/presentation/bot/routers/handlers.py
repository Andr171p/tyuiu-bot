from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command

from ..templates import START_TEMPLATE, INFO_TEMPLATE


handler_router = Router()


@handler_router.message(Command("start"))
async def start(message: Message) -> None:
    await message.answer(START_TEMPLATE)


@handler_router.message(Command("info"))
async def info(message: Message) -> None:
    await message.answer(INFO_TEMPLATE)
