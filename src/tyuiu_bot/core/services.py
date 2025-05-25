from typing import Optional

from uuid import UUID
from datetime import datetime

from .entities import Notification, User
from .dto import NotificationCreateDTO, UserContactDTO, SentNotificationDTO
from .interfaces import TelegramSender, UserRepository, UserRegistration, NotificationRepository
from ..constants import NOTIFICATION_STATUSES, USER_STATUSES


class NotificationService:
    def __init__(
            self,
            telegram_sender: TelegramSender,
            user_repository: UserRepository,
            notification_repository: NotificationRepository
    ) -> None:
        self._telegram_sender = telegram_sender
        self._user_repository = user_repository
        self._notification_repository = notification_repository

    async def notify(self, notification: Notification) -> SentNotificationDTO:
        user = await self._user_repository.get_by_user_id(notification.user_id)
        if not user:
            notification_id = await self._save(notification=notification, status="NOT_DELIVERED")
            return SentNotificationDTO(notification_id=notification_id, sent_at=datetime.now())
        message_id = await self._send(
            telegram_id=user.telegram_id,
            photo=notification.photo,
            text=notification.text
        )
        notification_id = await self._save(
            notification=notification,
            status="DELIVERED" if message_id else "ERROR",
            message_id=message_id
        )
        return SentNotificationDTO(notification_id=notification_id, sent_at=datetime.now())

    async def _send(self, telegram_id: int, photo: Optional[str], text: str) -> int:
        if photo:
            return await self._telegram_sender.send_with_photo(
                telegram_id=telegram_id,
                photo=photo,
                text=text
            )
        return await self._telegram_sender.send(telegram_id=telegram_id, text=text)

    async def _save(
            self,
            notification: Notification,
            status: NOTIFICATION_STATUSES,
            message_id: Optional[int] = None
    ) -> UUID:
        notification_dto = NotificationCreateDTO(
            level=notification.topic,
            user_id=notification.user_id,
            photo=notification.photo,
            text=notification.text,
            status=status,
            message_id=message_id
        )
        return await self._notification_repository.create(notification_dto)


class UserService:
    def __init__(
            self,
            user_repository: UserRepository,
            user_registration: UserRegistration
    ) -> None:
        self._user_repository = user_repository
        self._user_registration = user_registration

    async def subscribe(self, contact: UserContactDTO) -> USER_STATUSES:
        user = await self._user_repository.read(contact.telegram_id)
        if user:
            return "READY"
        user_id = await self._user_registration.get_user_id(contact.phone_number)
        status: USER_STATUSES = "READY" if user_id else "REGISTRATION_REQUIRE"
        user = User(
            telegram_id=contact.telegram_id,
            user_id=user_id,
            first_name=contact.first_name,
            last_name=contact.last_name,
            username=contact.username,
            phone_number=contact.phone_number,
            status=status
        )
        await self._user_repository.create(user)
        return status
