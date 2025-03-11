from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from aiogram.types import Message


class ChatBotPresenter:
    def __init__(self, message: "Message") -> None:
        self._message = message

    async def present(self, chatbot_message: str) -> None:
        await self._message.answer(chatbot_message)
