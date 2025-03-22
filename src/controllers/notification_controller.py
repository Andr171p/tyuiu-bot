from src.core.use_cases import NotificationUseCase
from src.schemas import DeliveredResponse, DeliveredResponsePresenter
from src.core.entities import NotificationAll, NotificationByPhoneNumber


class NotificationController:
    def __init__(self, notification_use_case: NotificationUseCase) -> None:
        self._notification_use_case = notification_use_case

    async def notify_all(self, notification: NotificationAll) -> DeliveredResponse:
        is_delivered = await self._notification_use_case.notify_all(notification)
        return DeliveredResponsePresenter(is_delivered).present()

    async def notify_by_phone_number(self, notification: NotificationByPhoneNumber) -> DeliveredResponse:
        is_delivered = await self._notification_use_case.notify(notification)
        return DeliveredResponsePresenter(is_delivered).present()
