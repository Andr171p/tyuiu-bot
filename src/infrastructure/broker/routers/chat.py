import logging

from faststream.rabbit import RabbitRouter
from dishka.integrations.base import FromDishka

from aiogram import Bot

from src.core.entities import AssistantMessage


logger = logging.getLogger(__name__)

chat_router = RabbitRouter()


@chat_router.subscriber("chat.assistant-messages")
async def answer(assistant_message: AssistantMessage, bot: FromDishka[Bot]) -> None:
    logger.info("Receive message %s", assistant_message)
    await bot.send_message(chat_id=int(assistant_message.chat_id), text=assistant_message.text)
    logger.info("Message sent successfully")
