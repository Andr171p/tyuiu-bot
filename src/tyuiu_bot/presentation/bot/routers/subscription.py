from aiogram import Router, F
from aiogram.types import Message
from aiogram.filters import Command

from dishka.integrations.aiogram import FromDishka

from src.tyuiu_bot.core.services import UserService
from src.tyuiu_bot.core.dto import UserContactDTO

from src.tyuiu_bot.settings import Settings
from src.tyuiu_bot.constants import SITE_URL

from ..keyboards import share_contact_keyboard, follow_to_register_keyboard


subscription_router = Router()


@subscription_router.message(Command("subscribe"))
async def subscription_details(message: Message, settings: FromDishka[Settings]) -> None:
    await message.answer(text=settings.messages.subscription, reply_markup=share_contact_keyboard())


@subscription_router.message(F.contact)
async def subscribe(message: Message, user_service: FromDishka[UserService]) -> None:
    contact = UserContactDTO(
        telegram_id=message.from_user.id,
        first_name=message.from_user.first_name,
        last_name=message.from_user.last_name,
        username=message.from_user.username,
        phone_number=message.contact.phone_number
    )
    status = await user_service.subscribe(contact)
    if status == "READY":
        await message.answer("Вы успешно поделились контактом")
    elif status == "REGISTRATION_REQUIRE":
        await message.answer(
            """<b>Контакт успешно отправлен.</b>
            Осталось зарегистрироваться на нашем сайте...
            """,
            reply_markup=follow_to_register_keyboard(SITE_URL)
        )
