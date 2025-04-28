from src.core.interfaces import Sender, ContactRepository
from src.core.entities import GlobalNotification, BroadcastNotification, DirectNotification


class NotificationService:
    def __init__(
            self,
            sender: Sender,
            contact_repository: ContactRepository
    ) -> None:
        self._sender = sender
        self._contact_repository = contact_repository

    async def notify(self, notification: DirectNotification) -> None:
        message = notification.message
        recipient = notification.recipient
        user_id = await self._contact_repository.read_user_id_by_phone_number(recipient.phone_number)
        await self._sender.send(
            user_id=user_id,
            text=message.text,
            photo_url=message.image_url,
            photo_base64=message.image_base64
        )

    async def notify_all(self, notification: GlobalNotification) -> None:
        message = notification.message
        user_ids = await self._contact_repository.list_user_ids()
        for user_id in user_ids:
            await self._sender.send(
                user_id=user_id,
                text=message.text,
                photo_url=message.image_url,
                photo_base64=message.image_base64
            )

    async def broadcast(self, notification: BroadcastNotification) -> None:
        message = notification.message
        recipients = notification.recipients
        for recipient in recipients:
            user_id = await self._contact_repository.read_user_id_by_phone_number(recipient.phone_number)
            await self._sender.send(
                user_id=user_id,
                text=message.text,
                photo_url=message.image_url,
                photo_base64=message.image_base64
            )
