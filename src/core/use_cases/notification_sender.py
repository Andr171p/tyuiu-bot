from src.core.entities import DirectedNotification, PublicNotification
from src.core.interfaces import AbstractSenderService
from src.repository import ContactRepository


class NotificationSender:
    def __init__(
            self,
            sender_service: AbstractSenderService,
            contact_repository: ContactRepository
    ) -> None:
        self._sender_service = sender_service
        self._contact_repository = contact_repository

    async def notify_direct(self, notification: DirectedNotification) -> None:
        recipients = notification.recipients
        content = notification.content
        for recipient in recipients:
            user_id = await self._contact_repository.get_user_id_by_phone_number(recipient.phone_number)
            await self._sender_service.send(
                user_id=user_id,
                text=content.text,
                photo_url=content.photo_url,
                photo_base64=content.photo_base64
            )

    async def notify_public(self, notification: PublicNotification) -> None:
        content = notification.content
        user_ids = await self._contact_repository.list_user_ids()
        for user_id in user_ids:
            await self._sender_service.send(
                user_id=user_id,
                text=content.text,
                photo_url=content.photo_url,
                photo_base64=content.photo_base64
            )
