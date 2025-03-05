from src.repository import DialogRepository
from src.dto import ChatHistoryPaginated, ChatHistory


class ChatHistoryUseCase:
    def __init__(self, dialog_repository: DialogRepository) -> None:
        self._dialog_repository = dialog_repository

    async def get_history_by_user_id(self, user_id: int) -> ChatHistory:
        ...

    async def get_paginated_history_by_user_id(self, user_id: int) -> ChatHistoryPaginated:
        ...

    async def get_total_count(self) -> int:
        ...

    async def get_count_by_user_id(self, user_id: int) -> int:
        ...
