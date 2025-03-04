from src.repository import ChatRepository
from src.dto import ChatHistoryPaginated, ChatHistory


class ChatHistoryUseCase:
    def __init__(self, chat_repository: ChatRepository) -> None:
        self._chat_repository = chat_repository

    async def get_history_by_user_id(self, user_id: int) -> ChatHistory:
        ...

    async def get_paginated_history_by_user_id(self, user_id: int) -> ChatHistoryPaginated:
        ...

    async def get_total_count(self) -> int:
        ...

    async def get_count_by_user_id(self, user_id: int) -> int:
        ...
