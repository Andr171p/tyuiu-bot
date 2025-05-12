from faststream import Logger
from faststream.rabbit import RabbitRouter

from dishka.integrations.base import FromDishka

from src.core.entities import Notification
from src.core.services import NotificationService


notifications_router = RabbitRouter()


@notifications_router.subscriber("telegram.notifications")
async def notify(
        notification: Notification,
        notification_service: FromDishka[NotificationService],
        logger: Logger
) -> None:
    logger.info("Receiving notification: %s", notification)
    await notification_service.notify(notification)
