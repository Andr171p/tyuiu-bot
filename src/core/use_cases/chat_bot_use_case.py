from datetime import datetime

from src.apis import ChatBotAPI
from src.repository import ChatRepository
from src.core.entities import Chat


class ChatBotUseCase:
    def __init__(
        self, 
        chat_bot_api: ChatBotAPI,
        chat_repository: ChatRepository
    ) -> None:
        self._chat_bot_api = chat_bot_api
        self._dialog_repository = chat_repository
        
    async def answer(self, user_id: int, question: str) -> str:
        answer = self._chat_bot_api.answer(question)
        chat = Chat(
            user_id=user_id,
            user_message=question,
            chat_bot_message=answer,
            created_at=datetime.now()
        )
        await self._chat_repository.add(chat)
        return answer
