from typing import Union

from src.core.use_cases import UsersUseCase
from src.core.entities import ChatHistory, ChatHistoryPage


class ChatsController:
    def __init__(self, users_use_case: UsersUseCase) -> None:
        self._users_use_case = users_use_case

    async def get_chat_history(
            self,
            user_id: int,
            is_paginated: bool,
            page: int,
            limit: int
    ) -> Union[ChatHistory, ChatHistoryPage]:
        if is_paginated:
            chat_history_page = await self._users_use_case.get_page_of_chat_history(
                user_id=user_id,
                page=page,
                limit=limit
            )
            return chat_history_page
        chat_history = await self._users_use_case.get_chat_history(user_id)
        return chat_history
