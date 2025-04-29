from aiogram import Router, F
from aiogram.types import Message
from aiogram.filters import Command
from dishka.integrations.aiogram import FromDishka

from src.settings import Settings
from src.core.services import UserService
from ..keyboards import share_contact_keyboard, follow_to_register_keyboard


subscription_router = Router()


@subscription_router.message(Command("subscribe"))
async def subscription_details(message: Message, settings: FromDishka[Settings]) -> None:
    await message.answer(text=settings.messages.subscription, reply_markup=share_contact_keyboard())


@subscription_router.message(F.contact)
async def share_contact(
        message: Message,
        user_service: FromDishka[UserService],
        settings: FromDishka[Settings]
) -> None:
    status = await user_service.share_contact(message.from_user.id, message.contact.phone_number)
    if status.SUCCESS:
        await message.answer("Вы успешно поделились контактом")
    elif status.ALREADY_SHARED:
        await message.answer("Вы уже поделились контактом")
    elif status.NOT_REGISTERED:
        await message.answer(
            """<b>Контакт успешно отправлен.</b>
            Осталось зарегистрироваться на нашем сайте...
            """,
            reply_markup=follow_to_register_keyboard(settings.main_site.url)
        )
    elif status.ERROR:
        await message.answer("Произошла ошибка, попробуйте позже...")
