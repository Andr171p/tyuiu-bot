from typing import Optional

from uuid import UUID
from datetime import datetime

from .entities import Notification, User
from .interfaces import TelegramSender, UserRepository, UserRegistration, NotificationRepository
from .dto import (
    NotificationCreateDTO,
    UserContactDTO,
    SentNotificationDTO,
    NewPasswordDTO,
    KEYBOARD,
    LEVEL_TO_KEYBOARD
)

from ..constants import NOTIFICATION_STATUS, USER_STATUS
from ..utils import get_password_hash
from ..settings import HashSettings


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
            text=notification.text,
            keyboard=LEVEL_TO_KEYBOARD.get(notification.level)
        )
        notification_id = await self._save(
            notification=notification,
            status="DELIVERED" if message_id else "ERROR",
            message_id=message_id
        )
        return SentNotificationDTO(notification_id=notification_id, sent_at=datetime.now())

    async def _send(
            self,
            telegram_id: int,
            photo: Optional[str],
            text: str,
            keyboard: Optional[KEYBOARD]
    ) -> Optional[int]:
        if photo:
            return await self._telegram_sender.send_with_photo(
                telegram_id=telegram_id,
                photo=photo,
                text=text,
                keyboard=keyboard
            )
        return await self._telegram_sender.send(
            telegram_id=telegram_id,
            text=text,
            keyboard=keyboard
        )

    async def _save(
            self,
            notification: Notification,
            status: NOTIFICATION_STATUS,
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


class SubscriptionService:
    def __init__(
            self,
            user_repository: UserRepository,
            user_registration: UserRegistration
    ) -> None:
        self._user_repository = user_repository
        self._user_registration = user_registration

    async def subscribe(self, contact: UserContactDTO) -> USER_STATUS:
        user = await self._user_repository.read(contact.telegram_id)
        if user:
            return "READY"
        user_id = await self._user_registration.get_user_id(contact.phone_number)
        status: USER_STATUS = "READY" if user_id else "REGISTRATION_REQUIRE"
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


class PasswordChangeService:
    def __init__(
            self,
            user_registration: UserRegistration,
            user_repository: UserRepository,
            hash_settings: HashSettings
    ) -> None:
        self._user_registration = user_registration
        self._user_repository = user_repository
        self._hash_settings = hash_settings

    async def change_password(self, new_password: NewPasswordDTO) -> bool:
        hashed_password = get_password_hash(
            password=new_password.confirm_password,
            secret_hash_key=self._hash_settings.SECRET_HASH_KEY
        )
        user = await self._user_repository.read(new_password.telegram_id)
        is_updated = await self._user_registration.update_password(
            user_id=user.user_id,
            hash_password=hashed_password
        )
        return is_updated
