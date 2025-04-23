from fastapi import APIRouter, status
from dishka.integrations.fastapi import FromDishka, DishkaRoute

from src.core.entities import User
from src.repository import UserRepository
from src.schemas import PerDayDistributionResponse

from src.presentation.api.v1.schemas import UsersResponse, CountResponse


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
    users = await user_repository.list()
    return UsersResponse(users=users)


@users_router.get(
    path="/count",
    response_model=CountResponse,
    status_code=status.HTTP_200_OK
)
async def get_count(user_repository: FromDishka[UserRepository]) -> CountResponse:
    count = await user_repository.count()
    return CountResponse(count=count)


@users_router.get(
    path="/date-to-count",
    response_model=PerDayDistributionResponse,
    status_code=status.HTTP_200_OK
)
async def get_date_to_count(
        user_repository: FromDishka[UserRepository]
) -> PerDayDistributionResponse:
    distribution = await user_repository.get_count_per_day()
    return PerDayDistributionResponse(distribution=distribution)


@users_router.get(
    path="/{user_id}",
    response_model=User,
    status_code=status.HTTP_200_OK
)
async def get_user(
        user_id: int,
        user_repository: FromDishka[UserRepository]
) -> User:
    return await user_repository.get(user_id)
