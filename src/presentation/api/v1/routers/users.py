from uuid import UUID

from fastapi import APIRouter, status, HTTPException

from dishka.integrations.fastapi import FromDishka, DishkaRoute

from src.core.dto import UserReadDTO
from src.core.interfaces import UserRepository, NotificationRepository

from ..schemas import PhoneNumberQuery, UserIdUpdate, UserNotificationsResponse


users_router = APIRouter(
    prefix="/api/v1/users",
    tags=["Telegram users"],
    route_class=DishkaRoute
)


@users_router.patch(
    path="/",
    status_code=status.HTTP_200_OK,
    response_model=UserReadDTO
)
async def update_user_id(
        phone_number: PhoneNumberQuery,
        user_id: UserIdUpdate,
        user_repository: FromDishka[UserRepository]
) -> UserReadDTO:
    user = await user_repository.update(phone_number, user_id=user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User has not yet shared contact")
    return user


@users_router.get(
    path="/notifications/{user_id}",
    status_code=status.HTTP_200_OK,
    response_model=UserNotificationsResponse
)
async def get_user_notifications(
        user_id: UUID,
        notification_repository: FromDishka[NotificationRepository]
) -> UserNotificationsResponse:
    notifications = await notification_repository.get_by_user_id(user_id)
    if not notifications:
        raise HTTPException(status_code=404, detail="Notifications not found")
    return UserNotificationsResponse(user_id=user_id, notifications=notifications)
