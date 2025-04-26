import logging

from typing import Union

from faststream import FastStream
from faststream.rabbit import RabbitBroker, RabbitRouter
from dishka.integrations.faststream import setup_dishka
from dishka.integrations.base import FromDishka

from src.ioc import container
from src.core.use_cases import NotificationSender
from src.core.entities import DirectedNotification, PublicNotification


logger = logging.getLogger(__name__)

tasks_router = RabbitRouter()


@tasks_router.subscriber("bot.tasks.notifications")
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


async def create_faststream_app() -> FastStream:
    broker = await container.get(RabbitBroker)
    broker.include_router(tasks_router)
    app = FastStream(broker)
    setup_dishka(
        container=container,
        app=app,
        auto_inject=True
    )
    return app
