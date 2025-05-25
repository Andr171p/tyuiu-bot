from faststream import Logger
from faststream.rabbit import RabbitRouter

from dishka.integrations.base import FromDishka

from src.tyuiu_bot.core.entities import Notification
from src.tyuiu_bot.core.dto import SentNotificationDTO
from src.tyuiu_bot.core.services import NotificationService


notifications_router = RabbitRouter()


@notifications_router.subscriber("telegram.notifications")
@notifications_router.publisher("telegram.sent-notifications")
async def notify(
        notification: Notification,
        notification_service: FromDishka[NotificationService],
        logger: Logger
) -> SentNotificationDTO:
    logger.info("Receiving notification: %s", notification)
    sent_notification = await notification_service.notify(notification)
    logger.info("Saved notification with id: %s", sent_notification.notification_id)
    return sent_notification
