from typing import Optional

from src.apis import ChatBotAPI
from src.repository import DialogRepository
from src.utils import chat_history_saver


class ChatBotUseCase:
    def __init__(
            self,
            chatbot_api: ChatBotAPI,
            dialog_repository: Optional[DialogRepository]
    ) -> None:
        self._chatbot_api = chatbot_api
        self._dialog_repository = dialog_repository

    @chat_history_saver
    async def answer(self, question: str, **kwargs) -> str:
        return await self._chatbot_api.answer(question)
