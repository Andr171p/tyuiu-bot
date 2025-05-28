from aiogram import F, Router
from aiogram.types import Message
from aiogram.filters import Command

from dishka.integrations.aiogram import FromDishka

from faststream.rabbit import RabbitBroker

from .templates import START_TEMPLATE, INFO_TEMPLATE, SUBSCRIPTION_DETAIL_TEMPLATE
from .keyboards import follow_to_register_keyboard, share_contact_keyboard
from src.tyuiu_bot.core.services import SubscriptionService
from src.tyuiu_bot.core.entities import UserMessage
from src.tyuiu_bot.core.dto import UserContactDTO
from src.tyuiu_bot.constants import SITE_URL


router = Router()


@router.message(Command("start"))
async def start(message: Message) -> None:
    await message.answer(START_TEMPLATE)


@router.message(Command("info"))
async def info(message: Message) -> None:
    await message.answer(INFO_TEMPLATE)


@router.message(Command("subscribe"))
async def subscription_details(message: Message) -> None:
    await message.answer(text=SUBSCRIPTION_DETAIL_TEMPLATE, reply_markup=share_contact_keyboard())


@router.message(F.contact)
async def subscribe(message: Message, subscription_service: FromDishka[SubscriptionService]) -> None:
    contact = UserContactDTO(
        telegram_id=message.from_user.id,
        first_name=message.from_user.first_name,
        last_name=message.from_user.last_name,
        username=message.from_user.username,
        phone_number=message.contact.phone_number
    )
    status = await subscription_service.subscribe(contact)
    if status == "READY":
        await message.answer("Вы успешно поделились контактом")
    elif status == "REGISTRATION_REQUIRE":
        await message.answer(
            """<b>Контакт успешно отправлен.</b>
            Осталось зарегистрироваться на нашем сайте...
            """,
            reply_markup=follow_to_register_keyboard(SITE_URL)
        )


@router.message(F.text)
async def chat(message: Message, broker: FromDishka[RabbitBroker]) -> None:
    await message.bot.send_chat_action(message.chat.id, "typing")
    user_message = UserMessage(chat_id=message.from_user.id, text=message.text)
    await broker.publish(user_message, queue="chat.user-messages")
