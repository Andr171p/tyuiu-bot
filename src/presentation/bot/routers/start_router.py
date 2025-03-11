from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command
from dishka.integrations.aiogram import FromDishka

from src.controllers import UsersController


start_router = Router()


@start_router.message(Command("start"))
async def start(
        message: Message,
        users_controller: FromDishka[UsersController]
) -> None:
    await users_controller.register_after_start(message)
