from typing import Optional

from uuid import UUID

from .entities import Notification
from .dto import NotificationCreateDTO
from .interfaces import TelegramSender, UserRepository, NotificationRepository
from ..constants import NOTIFICATION_STATUSES


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

    async def notify(self, notification: Notification) -> UUID:
        user = await self._user_repository.get_by_user_id(notification.user_id)
        if not user:
            return await self._save(notification=notification, status="NOT_DELIVERED")
        message_id = await self._send(
            telegram_id=user.telegram_id,
            photo=notification.photo,
            text=notification.text
        )
        return await self._save(
            notification=notification,
            status="DELIVERED" if message_id else "ERROR",
            message_id=message_id
        )

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
