from typing import List

from src.repository.base import BaseRepository
from src.database_old.crud import MessageCRUD
from src.database_old.models import Message
from src.schemas import MessageSchema


class MessageRepository(BaseRepository):
    crud = MessageCRUD()

    async def add(self, message: MessageSchema) -> MessageSchema:
        added_message = await self.crud.create(Message(**message.model_dump()))
        return MessageSchema(**added_message.__dict__)

    async def get_all(self) -> List[MessageSchema] | None:
        messages = await self.crud.read_all()
        if messages is None:
            return
        return [MessageSchema(**message.__dict__) for message in messages]
    
    async def get_by_user_id(self, user_id: int) -> List[MessageSchema] | None:
        messages = await self.crud.read_by_user_id(user_id)
        if messages is None:
            return
        return [MessageSchema(**message.__dict__) for message in messages]
    
    async def get_by_user_id_with_limit(
        self,
        user_id: int,
        page: int = 1,
        limit: int = 5
    ) -> List[MessageSchema] | None:
        messages = await self.crud.read_by_user_id_with_limit(
            user_id=user_id, 
            page=page, 
            limit=limit
        )
        if messages is None:
            return
        return [MessageSchema(**message.__dict__) for message in messages]
    
    async def get_count_by_user_id(self, user_id: int) -> int:
        messages_count = await self.crud.read_count_by_user_id(user_id)
        return messages_count
