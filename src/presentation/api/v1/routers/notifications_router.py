from typing import Union

from fastapi import APIRouter, status
from dishka.integrations.fastapi import FromDishka, DishkaRoute

from src.controllers import NotificationController
from src.core.entities import (
    NotificationAll,
    NotificationAllWithPhoto,
    NotificationByPhoneNumber,
    NotificationWithPhotoByPhoneNumber
)
from src.schemas import DeliveredResponse


notifications_router = APIRouter(
    prefix="/api/v1/notifications",
    tags=["Notifications"],
    route_class=DishkaRoute
)


@notifications_router.post(
    path="/",
    status_code=status.HTTP_200_OK,
    response_model=DeliveredResponse
)
async def notify(
        notification: Union[
            NotificationAll,
            NotificationAllWithPhoto,
            NotificationByPhoneNumber,
            NotificationWithPhotoByPhoneNumber
        ],
        notification_controller: FromDishka[NotificationController]
) -> DeliveredResponse:
    response = await notification_controller.notify(notification)
    return response
