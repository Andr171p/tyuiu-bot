import logging

from typing import Union

from faststream.rabbit import RabbitRouter
from dishka.integrations.base import FromDishka

from src.core.use_cases import NotificationSender
from src.core.entities import DirectedNotification, PublicNotification


logger = logging.getLogger(__name__)

notifications_router = RabbitRouter()


@notifications_router.subscriber("bot.tasks.notifications")
async def notify(
        notification: Union[DirectedNotification, PublicNotification],
        notification_sender: FromDishka[NotificationSender]
) -> None:
    if isinstance(notification, DirectedNotification):
        await notification_sender.notify_direct(notification)
        logger.info("Direct notification sent successfully")
    elif isinstance(notification, PublicNotification):
        await notification_sender.notify_public(notification)
        logger.info("Public notification sent successfully")
