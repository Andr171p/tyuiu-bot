from src.repository import ContactRepository
from src.core.interfaces import AbstractSenderService
from src.core.entities import Notification, SubscriberNotification


class NotificationSender:
    def __init__(
            self,
            sender_service: AbstractSenderService,
            contact_repository: ContactRepository
    ) -> None:
        self._sender_service = sender_service
        self._contact_repository = contact_repository

    async def notify_subscriber(self, subscriber_notification: SubscriberNotification) -> bool:
        phone_number = subscriber_notification.phone_number
        user_id = await self._contact_repository.get_user_id_by_phone_number(phone_number)
        return await self._sender_service.send(
            user_id=user_id,
            text=subscriber_notification.text,
            photo=subscriber_notification.photo
        )

    async def notify_users(self, notification: Notification) -> ...:
        ...
