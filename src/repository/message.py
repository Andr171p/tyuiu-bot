from src.core.database.service import MessageService
from src.core.database.models import Message
from src.schemas import MessageSchema


class MessageRepository:
    _message_service = MessageService()

    @classmethod
    async def add_message_by_user_id(
            cls,
            user_id: int,
            message: MessageSchema
    ) -> MessageSchema:
        added_message = await cls._message_service.add_message_by_user_id(
            user_id=user_id,
            message=Message(**message.dict())
        )
        return MessageSchema(**added_message.__dict__)
