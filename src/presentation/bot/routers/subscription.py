from datetime import datetime

from aiogram import Router, F
from aiogram.types import Message
from aiogram.filters import Command
from dishka.integrations.aiogram import FromDishka

from src.settings import Settings
from src.core.entities import Contact
from src.core.use_cases import UserManager
from src.presentation.bot.keyboards import share_contact_keyboard


subscription_router = Router()


@subscription_router.message(Command("subscribe"))
async def subscription_details(message: Message, settings: FromDishka[Settings]) -> None:
    await message.answer(text=settings.messages.subscription, reply_markup=share_contact_keyboard())


@subscription_router.message(F.contact)
async def share_contact(message: Message, user_manager: FromDishka[UserManager]) -> None:
    user_id = message.from_user.id
    phone_number = message.contact.phone_number
    is_exists = await user_manager.is_exists(user_id)
    contact = Contact(
        user_id=user_id,
        phone_number=phone_number,
        is_exists=is_exists,
        created_at=datetime.now()
    )
    await user_manager.share_contact(contact)
    await message.answer("Вы успешно поделились контактом")
