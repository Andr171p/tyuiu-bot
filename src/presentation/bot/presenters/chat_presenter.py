from aiogram.types import Message

from src.presentation.bot.presenters.base_presenter import BasePresenter


class ChatPresenter(BasePresenter):
    @classmethod
    async def present(cls, message: Message, **kwargs) -> None:
        answer = kwargs.get("answer")
        await message.answer(answer)
