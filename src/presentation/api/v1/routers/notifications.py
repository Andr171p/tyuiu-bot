from uuid import UUID

from fastapi import APIRouter, status, HTTPException

from dishka.integrations.fastapi import FromDishka, DishkaRoute

from src.core.entities import Notification
from src.core.dto import NotificationReadDTO
from src.core.services import NotificationService
from src.core.interfaces import NotificationRepository

from ..schemas import CreatedNotificationResponse


notifications_router = APIRouter(
    prefix="/api/v1/notifications",
    tags=["Notifications"],
    route_class=DishkaRoute
)


@notifications_router.post(
    path="/",
    status_code=status.HTTP_201_CREATED,
    response_model=CreatedNotificationResponse
)
async def notify(
        notification: Notification,
        notification_service: FromDishka[NotificationService]
) -> CreatedNotificationResponse:
    notification_id = await notification_service.notify(notification)
    return CreatedNotificationResponse(notification_id=notification_id)


@notifications_router.get(
    path="/{notification_id}",
    status_code=status.HTTP_200_OK,
    response_model=NotificationReadDTO
)
async def get_notification(
        notification_id: UUID,
        notification_repository: FromDishka[NotificationRepository]
) -> NotificationReadDTO:
    notification = await notification_repository.read(notification_id)
    if not notification:
        raise HTTPException(status_code=404, detail="Notification not found")
    return notification
