from datetime import datetime

from aiogram import F, Router
from aiogram.types import Message

from dishka.integrations.aiogram import FromDishka

from src.schemas import MessageSchema
from src.services import ChatService


chat_router = Router()


@chat_router.message(F.text)
async def get_answer_on_question(
        message: Message,
        chat_service: FromDishka[ChatService],
) -> None:
    await message.bot.send_chat_action(message.chat.id, "typing")
    user_id: int = message.from_user.id
    question: str = message.text
    answer = await chat_service.answer_on_question(question)
    dialog = MessageSchema(
        user_id=user_id,
        user_message=question,
        bot_message=answer,
        created_at=datetime.now()
    )
    await chat_service.save_dialog(dialog)
    await message.reply(answer)
