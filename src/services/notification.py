import logging
from typing import List

from aiogram import Bot

from src.schemas import ContactSchema
from src.repository import ContactRepository
from src.services.sender import SenderService


log = logging.getLogger(__name__)


class NotificationService:
    contact_repository = ContactRepository()

    @classmethod
    async def subscribe(cls, contact: ContactSchema) -> None:
        if await cls.contact_repository.get_by_user_id(contact.user_id) is not None:
            log.info("User already subscribed")
            return
        subscribed_contact = await cls.contact_repository.add(contact)
        log.info(
            "User with %s successfully subscribed contact %s",
            subscribed_contact.user_id,
            subscribed_contact.phone_number
        )

    @classmethod
    async def notify_by_phone_number(
            cls,
            phone_number: str,
            text: str,
            bot: Bot
    ) -> ContactSchema | None:
        contact = await cls.contact_repository.get_by_phone_number(phone_number)
        user_id: int = contact.user_id
        sender_service = SenderService(bot)
        await sender_service.send_message(
            user_id=user_id,
            text=text
        )
        log.info("Successfully sent notification to user with %s", user_id)
        return contact

    @classmethod
    async def notify_all_subscribers(
            cls,
            text: str,
            bot: Bot
    ) -> List[ContactSchema] | None:
        subscribers = await cls.contact_repository.get_all()
        user_ids = [subscriber.user_id for subscriber in subscribers]
        sender_service = SenderService(bot)
        await sender_service.send_message_to_users(
            user_ids=user_ids,
            text=text
        )
        log.info("Successfully sent notification to subscribers")
        return subscribers
