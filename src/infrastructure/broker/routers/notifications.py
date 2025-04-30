import logging

from typing import Union

from faststream.rabbit import RabbitRouter
from dishka.integrations.base import FromDishka

from src.core.services import NotificationService
from src.core.entities import NotificationOne, NotificationAll, NotificationBatch


logger = logging.getLogger(__name__)

notifications_router = RabbitRouter()


@notifications_router.subscriber("bot.tasks.notifications")
async def notify(
        notification: Union[NotificationOne, NotificationAll, NotificationBatch],
        notification_service: FromDishka[NotificationService]
) -> None:
    if isinstance(notification, NotificationOne):
        await notification_service.notify_one(notification)
    elif isinstance(notification, NotificationAll):
        await notification_service.notify_all(notification)
    elif isinstance(notification, NotificationBatch):
        await notification_service.notify_batch(notification)
    logger.info("Notification sent successfully")
