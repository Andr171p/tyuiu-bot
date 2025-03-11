from typing import Union

from src.core.use_cases import NotificationUseCase
from src.core.entities import (
    NotificationAll,
    NotificationAllWithPhoto,
    NotificationByPhoneNumber,
    NotificationWithPhotoByPhoneNumber
)
from src.schemas import DeliveredResponse, DeliveredResponsePresenter


class NotificationController:
    def __init__(self, notification_use_case: NotificationUseCase) -> None:
        self._notification_use_case = notification_use_case

    async def notify(
            self,
            notification: Union[
                NotificationAll,
                NotificationByPhoneNumber,
                NotificationAllWithPhoto,
                NotificationWithPhotoByPhoneNumber
            ]
    ) -> DeliveredResponse:
        is_delivered: bool = False
        if isinstance(notification, NotificationAll):
            is_delivered = await self._notification_use_case.notify_all(notification)
        elif isinstance(notification, NotificationByPhoneNumber):
            is_delivered = await self._notification_use_case.notify(notification)
        elif isinstance(notification, NotificationAllWithPhoto):
            is_delivered = await self._notification_use_case.notify_all_with_photo(notification)
        elif isinstance(notification, NotificationWithPhotoByPhoneNumber):
            is_delivered = await self._notification_use_case.notify_with_photo(notification)
        return DeliveredResponsePresenter(is_delivered).present()
