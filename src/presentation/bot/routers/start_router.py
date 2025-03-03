from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command

from dishka.integrations.aiogram import FromDishka

from src.core.use_cases import UsersUseCase
from src.mappers import UserMapper
from src.presentation.bot.presenters import StartPresenter


start_router = Router()


@start_router.message(Command("start"))
async def start(message: Message, users: FromDishka[UsersUseCase]) -> None:
    user = UserMapper.from_message(message)
    await users.register(user)
    await StartPresenter.present(message)
