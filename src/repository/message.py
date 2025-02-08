from typing import List

from src.repository.base import BaseRepository
from src.database.crud import MessageCRUD
from src.database.models import Message
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
