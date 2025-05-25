from uuid import UUID

from fastapi import APIRouter, status, HTTPException

from dishka.integrations.fastapi import FromDishka, DishkaRoute

from src.tyuiu_bot.core.entities import Notification
from src.tyuiu_bot.core.services import NotificationService
from src.tyuiu_bot.core.interfaces import NotificationRepository
from src.tyuiu_bot.core.dto import NotificationReadDTO, SentNotificationDTO


notifications_router = APIRouter(
    prefix="/api/v1/notifications",
    tags=["Notifications"],
    route_class=DishkaRoute
)


@notifications_router.post(
    path="/",
    status_code=status.HTTP_201_CREATED,
    response_model=SentNotificationDTO
)
async def notify(
        notification: Notification,
        notification_service: FromDishka[NotificationService]
) -> SentNotificationDTO:
    sent_notification = await notification_service.notify(notification)
    if not sent_notification:
        raise HTTPException(status_code=500, detail="Error while sending notification")
    return sent_notification


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
