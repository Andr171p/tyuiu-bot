from faststream import Logger
from faststream.rabbit import RabbitRouter

from dishka.integrations.base import FromDishka

from aiogram import Bot

from src.tyuiu_bot.core.entities import AssistantMessage


chat_router = RabbitRouter()


@chat_router.subscriber("chat.assistant-messages")
async def answer(
        assistant_message: AssistantMessage,
        bot: FromDishka[Bot],
        logger: Logger
) -> None:
    logger.info("Receive message %s", assistant_message)
    await bot.send_message(chat_id=assistant_message.chat_id, text=assistant_message.text)
    logger.info("Message sent successfully")
