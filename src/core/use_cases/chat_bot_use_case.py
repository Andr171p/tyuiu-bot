from datetime import datetime

from src.apis import ChatBotAPI
from src.repository import ChatRepository
from src.core.entities import Chat
from src.dto import ChatHistory, ChatHistoryPaginated


class ChatBotUseCase:
    def __init__(
        self, 
        chat_bot_api: ChatBotAPI,
        chat_repository: ChatRepository
    ) -> None:
        self._chat_bot_api = chat_bot_api
        self._chat_repository = chat_repository
        
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
    
    async def get_chat_history(self, user_id: int) -> ChatHistory:
        chats = await self._chat_repository.get_by_user_id(user_id)
        return ChatHistory(
            user_id=user_id,
            chats=chats
        )
        
    async def get_page_of_chat_history(
        self, 
        user_id: int,
        page: int,
        limit: int = 5
    ) -> ChatHistoryPaginated:
        chats = await self._chat_repository.get_by_user_id_with_limit(
            user_id=user_id,
            page=page,
            limit=limit
        )
        return ChatHistoryPaginated(
            user_id=user_id,
            page=page,
            limit=limit,
            chats=chats
        )
        