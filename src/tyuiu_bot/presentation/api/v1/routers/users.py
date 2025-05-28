from uuid import UUID

from fastapi import APIRouter, status, HTTPException

from dishka.integrations.fastapi import FromDishka, DishkaRoute

from src.tyuiu_bot.core.dto import UserReadDTO, NotificationReadDTO
from src.tyuiu_bot.core.interfaces import UserRepository, NotificationRepository

from ..schemas import PhoneNumberQuery, UserIdUpdate


users_router = APIRouter(
    prefix="/api/v1/users",
    tags=["Telegram users"],
    route_class=DishkaRoute
)


@users_router.get(
    path="/{user_id}",
    status_code=status.HTTP_200_OK,
    response_model=UserReadDTO
)
async def get_user(user_id: UUID, user_repository: FromDishka[UserRepository]) -> UserReadDTO:
    user = await user_repository.get_by_user_id(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user


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
    path="/{user_id}/notifications",
    status_code=status.HTTP_200_OK,
    response_model=list[NotificationReadDTO]
)
async def get_user_notifications(
        user_id: UUID,
        notification_repository: FromDishka[NotificationRepository]
) -> list[NotificationReadDTO]:
    notifications = await notification_repository.get_by_user_id(user_id)
    if not notifications:
        raise HTTPException(status_code=404, detail="Notifications not found")
    return notifications
