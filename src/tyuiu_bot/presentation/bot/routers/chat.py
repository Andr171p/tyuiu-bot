from aiogram import F, Router
from aiogram.types import Message

from dishka.integrations.aiogram import FromDishka

from faststream.rabbit import RabbitBroker

from src.tyuiu_bot.core.entities import UserMessage


chat_router = Router()


@chat_router.message(F.text)
async def answer(message: Message, broker: FromDishka[RabbitBroker]) -> None:
    await message.bot.send_chat_action(message.chat.id, "typing")
    user_message = UserMessage(chat_id=message.from_user.id, text=message.text)
    await broker.publish(user_message, queue="chat.user-messages")
