from aiogram import F, Router
from aiogram.types import Message
from dishka.integrations.aiogram import FromDishka

from src.core.use_cases import ChatAssistant


chat_router = Router()


@chat_router.message(F.text)
async def answer(message: Message, chatbot_assistant: FromDishka[ChatAssistant]) -> None:
    text = await chatbot_assistant.answer(str(message.from_user.id), message.text)
    await message.answer(text)
