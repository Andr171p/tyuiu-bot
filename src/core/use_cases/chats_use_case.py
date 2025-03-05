from typing import List

from src.repository import DialogRepository
from src.dto import ChatPaginated
from src.core.entities import Chat, Dialog


class ChatsUseCase:
    def __init__(self, dialog_repository: DialogRepository) -> None:
        self._dialog_repository = dialog_repository

    async def get_dialogs_history(self) -> List[Dialog]:
        dialogs = await self._dialog_repository.get_all()
        return dialogs

    async def get_history_by_user_id(self, user_id: int) -> Chat:
        dialogs = await self._dialog_repository.get_by_user_id(user_id)
        return Chat(user_id=user_id, dialogs=dialogs)

    async def get_paginated_history_by_user_id(
            self,
            user_id: int,
            page: int,
            limit: int = 5
    ) -> ChatPaginated:
        dialogs = await self._dialog_repository.get_by_user_id_with_limit(
            user_id=user_id,
            page=page,
            limit=limit
        )
        dialogs_count = await self.get_total_dialogs_count()
        return ChatPaginated(
            user_id=user_id,
            total=dialogs_count,
            page=page,
            limit=limit,
            dialogs=dialogs
        )

    async def get_total_dialogs_count(self) -> int:
        return await self._dialog_repository.get_total_count()

    async def get_dialogs_count_by_user_id(self, user_id: int) -> int:
        return await self._dialog_repository.get_count_by_user_id(user_id)
