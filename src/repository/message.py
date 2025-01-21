from src.repository.base import BaseRepository
from src.database.crud import MessageCRUD
from src.database.models import Message
from src.schemas import MessageSchema


class MessageRepository(BaseRepository):
    crud = MessageCRUD()

    async def add(self, message: MessageSchema) -> MessageSchema:
        added_message = await self.crud.create(Message(**message.dict()))
        return MessageSchema(**added_message.__dict__)
