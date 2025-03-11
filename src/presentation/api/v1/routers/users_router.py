from fastapi import APIRouter, status
from dishka.integrations.fastapi import FromDishka, DishkaRoute

from src.repository import UserRepository
from src.core.entities import User
from src.schemas import UsersResponse, UsersCountResponse, PerDayDistributionResponse


users_router = APIRouter(
    prefix="/api/v1/users",
    tags=["Users"],
    route_class=DishkaRoute
)


@users_router.get(
    path="/",
    response_model=UsersResponse,
    status_code=status.HTTP_200_OK
)
async def get_users(user_repository: FromDishka[UserRepository]) -> UsersResponse:
    users = await user_repository.get_all()
    return UsersResponse(users=users)


@users_router.get(
    path="/count/",
    response_model=UsersCountResponse,
    status_code=status.HTTP_200_OK
)
async def get_users_count(user_repository: FromDishka[UserRepository]) -> UsersCountResponse:
    users_count = await user_repository.get_total_count()
    return UsersCountResponse(count=users_count)


@users_router.get(
    path="/{user_id}/",
    response_model=User,
    status_code=status.HTTP_200_OK
)
async def get_user_by_user_id(
        user_id: int,
        user_repository: FromDishka[UserRepository]
) -> User:
    user = await user_repository.get_by_user_id(user_id)
    return user


@users_router.get(
    path="/per-day-count/",
    response_model=PerDayDistributionResponse,
    status_code=status.HTTP_200_OK
)
async def get_per_day_count_distribution(
        user_repository: FromDishka[UserRepository]
) -> PerDayDistributionResponse:
    distribution = await user_repository.get_count_per_day()
    return PerDayDistributionResponse(distribution=distribution)
