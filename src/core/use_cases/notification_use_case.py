from src.core.entities import (
    NotificationAll,
    NotificationAllWithPhoto,
    NotificationByPhoneNumber,
    NotificationWithPhotoByPhoneNumber
)
from src.services.sender import BaseSenderService
from src.repository import ContactRepository


class NotificationUseCase:
    def __init__(
            self,
            sender_service: BaseSenderService,
            contact_repository: ContactRepository
    ) -> None:
        self._sender_service = sender_service
        self._contact_repository = contact_repository

    async def notify(self, notification: NotificationByPhoneNumber) -> bool:
        user_id: int = await self._contact_repository.get_user_id_by_phone_number(notification.phone_number)
        return await self._sender_service.send_message(
            user_id=user_id,
            text=notification.text
        )

    async def notify_with_photo(self, notification: NotificationWithPhotoByPhoneNumber) -> bool:
        user_id: int = await self._contact_repository.get_user_id_by_phone_number(notification.phone_number)
        return await self._sender_service.send_message_with_photo(
            user_id=user_id,
            photo=notification.photo,
            text=notification.text
        )

    async def notify_all(self, notification: NotificationAll) -> ...:
        user_ids = await self._contact_repository.get_all_user_ids()
        for user_id in user_ids:
            await self._sender_service.send_message(
                user_id=user_id,
                text=notification.text
            )

    async def notify_all_with_photo(self, notification: NotificationAllWithPhoto) -> ...:
        user_ids = await self._contact_repository.get_all_user_ids()
        for user_id in user_ids:
            await self._sender_service.send_message_with_photo(
                user_id=user_id,
                photo=notification.photo,
                text=notification.text
            )
