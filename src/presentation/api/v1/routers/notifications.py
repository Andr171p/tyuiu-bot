from typing import Union

from fastapi import APIRouter, status, BackgroundTasks
from dishka.integrations.fastapi import FromDishka, DishkaRoute

from faststream.rabbit import RabbitBroker

from src.core.entities import DirectedNotification, PublicNotification
from src.presentation.api.v1.schemas import SentNotificationResponse


notifications_router = APIRouter(
    prefix="/api/v1/notifications",
    tags=["Notifications"],
    route_class=DishkaRoute
)


@notifications_router.post(
    path="/",
    response_model=SentNotificationResponse,
    status_code=status.HTTP_201_CREATED
)
async def notify(
        notification: Union[DirectedNotification, PublicNotification],
        background_tasks: BackgroundTasks,
        broker: FromDishka[RabbitBroker]
) -> SentNotificationResponse:
    background_tasks.add_task(
        broker.publish,
        notification,
        queue="chat.tasks.messages",
    )
    return SentNotificationResponse()
