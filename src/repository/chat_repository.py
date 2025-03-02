from typing import TYPE_CHECKING, List, Union

if TYPE_CHECKING:
    from src.database.crud import ChatCRUD

from src.repository.base_repository import BaseRepository
from src.database.models import ChatModel
from src.core.entities import Chat


class ChatRepository(BaseRepository):
    def __init__(self, crud: "ChatCRUD") -> None:
        self._crud = crud
        
    async def save(self, chat: Chat) -> int:
        id = await self._crud.create(ChatModel(**chat.model_dump()))
        return id

    async def get_by_user_id(self, user_id: int) -> Union[Chat, None]:
        chat = await self._crud.read_by_user_id(user_id)
        return Chat.model_validate(chat) if chat else None
    
    async def get_by_user_id_with_limit(
        self,
        user_id: int,
        page: int = 1,
        limit: int = 5
    ) -> List[Union[Chat, None]]:
        chats = await self._crud.read_by_user_id_with_limit(
            user_id=user_id, 
            page=page, 
            limit=limit
        )
        return [Chat.model_validate(chat) for chat in chats] if chats else []
    
    async def get_all(self) -> List[Union[Chat, None]]:
        chats = await self._crud.read_all()
        return [Chat.model_validate(chat) for chat in chats] if chats else []
    
    async def get_count_by_user_id(self, user_id: int) -> int:
        count = await self._crud.read_count_by_user_id(user_id)
        return count if count else 0
    
    async def get_total_count(self) -> Union[int, None]:
        count = await self._crud.read_total_count()
        return count if count else 0
    