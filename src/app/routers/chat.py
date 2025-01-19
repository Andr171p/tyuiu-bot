from aiogram import F, Router
from aiogram.types import Message

from dishka.integrations.aiogram import FromDishka

from src.services import ChatService, AnalyticsService


chat_router = Router()


@chat_router.message(F.text)
async def get_answer_on_question(
        message: Message,
        chat_service: FromDishka[ChatService],
        analytics_service: FromDishka[AnalyticsService]
) -> None:
    await message.bot.send_chat_action(message.chat.id, "typing")
    user_id: int = message.from_user.id
    question: str = message.text
    response = await chat_service.get_answer_on_question(question)
    await analytics_service.save_message_by_user_id(
        user_id=user_id,
        user_message=question,
        bot_message=response.data.answer
    )
    await message.reply(response.data.answer)
