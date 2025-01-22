import logging
from datetime import datetime

from aiogram import Bot
from aiogram.types import Message

from src.schemas import ContactSchema
from src.repository import ContactRepository
from src.services.sender import SenderService


log = logging.getLogger(__name__)


class NotificationService:
    contact_repository = ContactRepository()

    @classmethod
    async def subscribe(cls, message: Message) -> None:
        user_id: int = message.from_user.id
        phone_number: str = message.contact.phone_number
        if await cls.contact_repository.get_by_user_id(user_id) is not None:
            log.info("User already subscribed")
            return
        contact = ContactSchema(
            user_id=user_id,
            phone_number=phone_number,
            created_at=datetime.now()
        )
        subscribed_contact = await cls.contact_repository.add(contact)
        log.info(
            "User with %s successfully subscribed contact %s",
            subscribed_contact.user_id,
            subscribed_contact.phone_number
        )

    @classmethod
    async def send_notification_by_phone_number(
            cls,
            phone_number: str,
            text: str,
            bot: Bot
    ) -> None:
        contact = await cls.contact_repository.get_by_phone_number(phone_number)
        user_id: int = contact.user_id
        sender_service = SenderService(bot)
        await sender_service.send_message(
            user_id=user_id,
            text=text
        )
        log.info("Successfully sent notification to user with %s", user_id)

    @classmethod
    async def send_notification_to_all_subscribers(
            cls,
            text: str,
            bot: Bot
    ) -> None:
        subscribers = await cls.contact_repository.get_all()
        user_ids = [subscriber.user_id for subscriber in subscribers]
        sender_service = SenderService(bot)
        await sender_service.send_message_to_users(
            user_ids=user_ids,
            text=text
        )
        log.info("Successfully sent notification to subscribers")
