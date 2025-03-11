from aiogram import Router, F
from aiogram.types import Message
from aiogram.filters import Command
from dishka.integrations.aiogram import FromDishka

from src.controllers import UsersController
from src.presenters import GetShareContactDetailsPresenter


contact_router = Router()


@contact_router.message(Command("share_contact"))
async def get_share_contact_details(message: Message) -> None:
    await GetShareContactDetailsPresenter(message=message).present()


@contact_router.message(F.contact)
async def share_contact(
        message: Message,
        users_controller: FromDishka[UsersController]
) -> None:
    await users_controller.share_contact(message)
