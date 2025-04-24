from aiogram import F, Router
from aiogram.types import Message
from dishka.integrations.aiogram import FromDishka

from src.settings import Settings
from src.core.use_cases import ChatAssistant


chat_router = Router()


@chat_router.message(F.text)
async def answer(
        message: Message,
        chat_assistant: FromDishka[ChatAssistant],
        settings: FromDishka[Settings]
) -> None:
    await message.bot.send_chat_action(message.chat.id, "typing")
    text = await chat_assistant.answer(str(message.from_user.id), message.text)
    if text is None:
        await message.answer(settings.messages.error)
    else:
        await message.answer(text)
