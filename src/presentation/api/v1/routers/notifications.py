from typing import Union

from fastapi import APIRouter, status, BackgroundTasks, Response
from dishka.integrations.fastapi import FromDishka, DishkaRoute

from faststream.rabbit import RabbitBroker

from src.core.entities import NotificationOne, NotificationAll, NotificationBatch


notifications_router = APIRouter(
    prefix="/api/v1/notifications",
    tags=["Notifications"],
    route_class=DishkaRoute
)


@notifications_router.post("/")
async def notify(
        notification: Union[NotificationOne, NotificationAll, NotificationBatch],
        background_tasks: BackgroundTasks,
        broker: FromDishka[RabbitBroker]
) -> Response:
    background_tasks.add_task(
        broker.publish,
        notification,
        queue="chat.tasks.messages",
    )
    return Response(status_code=status.HTTP_202_ACCEPTED)
