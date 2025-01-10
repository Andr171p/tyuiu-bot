import logging
from datetime import datetime

from aiogram.types import Message

from src.schemas import UserSchema, MessageSchema
from src.repository import UserRepository, MessageRepository


log = logging.getLogger(__name__)


class AnalyticsService:
    async def register_user_by_message(
            self,
            message: Message
    ) -> "AnalyticsService":
        user = UserSchema(
            user_id=message.from_user.id,
            username=message.from_user.username,
            created_at=datetime.now()
        )
        registered_user = await UserRepository.add_user(user)
        log.info("User %s registered successfully", registered_user)
        return self

    async def save_message_by_user_id(
            self,
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
        saved_message = await MessageRepository.add_message_by_user_id(
            user_id=user_id,
            message=message
        )
        log.info("Message %s message saved successfully", saved_message)
        return self
