from datetime import datetime

from aiogram import Router
from aiogram.types.message import Message
from aiogram.filters import Command

from src.schemas import UserSchema
from src.repository import UserRepository


start_router = Router()


@start_router.message(Command("start"))
async def start(message: Message) -> None:
    user_id: int = message.from_user.id
    username: str | None = message.from_user.username
    user = UserSchema(
        user_id=user_id,
        username=username,
        created_at=datetime.now()
    )
    _ = await UserRepository.add_user(user)
