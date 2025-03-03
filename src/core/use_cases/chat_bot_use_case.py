from typing import Optional

from src.apis import ChatBotAPI
from src.repository import ChatRepository
from src.utils import chat_saver


class ChatBotUseCase:
    def __init__(self, chat_bot_api: ChatBotAPI, **kwargs) -> None:
        self._chat_bot_api = chat_bot_api
        self._chat_repository: Optional[ChatRepository] = kwargs.get("chat_repository")

    def __post_init__(self) -> None:
        self.answer = chat_saver(self._chat_repository)(self.answer)

    @chat_saver(chat_repository=None)
    async def answer(self, question: str, **kwargs) -> str:
        answer = await self._chat_bot_api.answer(question)
        return answer
