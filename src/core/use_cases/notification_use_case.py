from src.dto import NotificationByPhoneNumber, NotificationWithPhotoByPhoneNumber
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
        ...

    async def notify_with_photo(self, notification: NotificationWithPhotoByPhoneNumber) -> bool:
        ...

    async def notify_all(self) -> ...:
        ...
