from aiogram import F, Router
from aiogram.types import Message

from dishka.integrations.aiogram import FromDishka

from src.core.use_cases import ChatBotUseCase
from src.presentation.bot.presenters import ChatPresenter


chatbot_router = Router()


@chatbot_router.message(F.text)
async def answer(message: Message, chatbot: FromDishka[ChatBotUseCase]) -> None:
    await message.bot.send_chat_action(message.chat.id, "typing")
    user_question: str = message.text
    chatbot_answer = await chatbot.answer(user_question)
    await ChatPresenter.present(message, answer=chatbot_answer)
