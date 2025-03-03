from src.apis import ChatBotAPI
from src.repository import ChatRepository
from src.utils import chat_saver


class ChatBotUseCase:
    def __init__(self, chat_bot_api: ChatBotAPI) -> None:
        self._chat_bot_api = chat_bot_api

    async def answer(self, question: str) -> str:
        answer = await self._chat_bot_api.answer(question)
        return answer
