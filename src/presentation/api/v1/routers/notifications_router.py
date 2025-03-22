from fastapi import APIRouter, status
from dishka.integrations.fastapi import FromDishka, DishkaRoute

from src.schemas import DeliveredResponse
from src.controllers import NotificationController
from src.core.entities import NotificationAll, NotificationByPhoneNumber


notifications_router = APIRouter(
    prefix="/api/v1/notifications",
    tags=["Notifications"],
    route_class=DishkaRoute
)


@notifications_router.post(
    path="/notify-all/",
    status_code=status.HTTP_200_OK,
    response_model=DeliveredResponse
)
async def notify_all(
        notification: NotificationAll,
        notification_controller: FromDishka[NotificationController]
) -> DeliveredResponse:
    response = await notification_controller.notify_all(notification)
    return response


@notifications_router.post(
    path="/notify-by-phone-number",
    status_code=status.HTTP_200_OK,
    response_model=DeliveredResponse
)
async def notify_by_phone_number(
        notification: NotificationByPhoneNumber,
        notification_controller: FromDishka[NotificationController]
) -> DeliveredResponse:
    response = await notification_controller.notify_by_phone_number(notification)
    return response
