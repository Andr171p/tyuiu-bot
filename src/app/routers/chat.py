from aiogram import F, Router
from aiogram.types import Message

from src.services import RAGAPIService, AnalyticsService


chat_router = Router()


@chat_router.message(F.text)
async def get_answer_on_question(message: Message) -> None:
    user_id: int = message.from_user.id
    question: str = message.text
    response = await RAGAPIService().get_answer(question)
    await AnalyticsService().save_message_by_user_id(
        user_id=user_id,
        user_message=question,
        bot_message=response.data.answer
    )
    await message.reply(response.data.answer)
