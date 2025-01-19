import logging
from datetime import datetime

from aiogram.types import Message

from src.schemas import UserSchema, MessageSchema
from src.repository import UserRepository, MessageRepository


log = logging.getLogger(__name__)


class AnalyticsService:
    user_repository = UserRepository()
    message_repository = MessageRepository()

    @classmethod
    async def register_user_by_message(
            cls,
            message: Message
    ) -> "AnalyticsService":
        if await cls.user_repository.get_user_by_user_id(message.from_user.id) is not None:
            return cls()
        user = UserSchema(
            user_id=message.from_user.id,
            username=message.from_user.username,
            created_at=datetime.now()
        )
        registered_user = await cls.user_repository.add_user(user)
        log.info("User %s registered successfully", registered_user)
        return cls()

    @classmethod
    async def save_message_by_user_id(
            cls,
            user_id: int,
            user_message: str,
            bot_message: str,
            created_at: datetime = datetime.now()
    ) -> "AnalyticsService":
        message = MessageSchema(
            user_message=user_message,
            bot_message=bot_message,
            created_at=created_at
        )
        saved_message = await cls.message_repository.add_message_by_user_id(
            user_id=user_id,
            message=message
        )
        log.info("Message %s message saved successfully", saved_message)
        return cls()
