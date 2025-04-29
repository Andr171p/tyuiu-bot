from typing import Union

from fastapi import APIRouter, status, Query, HTTPException
from dishka.integrations.fastapi import FromDishka, DishkaRoute

from src.core.entities import CreatedUser
from src.core.interfaces import UserRepository
from ..schemas import (
    PhoneNumberQuery,
    UsersResponse,
    UsersPageResponse,
    UserUpdate,
    CountResponse,
    DailyCount,
    DailyCountResponse
)


users_router = APIRouter(
    prefix="/api/v1/users",
    tags=["Users"],
    route_class=DishkaRoute
)


@users_router.get(
    path="/",
    response_model=Union[UsersResponse, UsersPageResponse],
    status_code=status.HTTP_200_OK
)
async def get_users(
        user_repository: FromDishka[UserRepository],
        is_paginated: bool = Query(default=True),
        page: int = Query(ge=1, default=1),
        limit: int = Query(ge=1, default=10)
) -> Union[UsersResponse, UsersPageResponse]:
    if is_paginated:
        total = await user_repository.count()
        users = await user_repository.paginate(page, limit)
        return UsersPageResponse(
            total=total,
            page=page,
            limit=limit,
            users=users
        )
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
    path="/count-daily",
    response_model=DailyCountResponse,
    status_code=status.HTTP_200_OK
)
async def get_count_daily(
        user_repository: FromDishka[UserRepository]
) -> DailyCountResponse:
    counts = await user_repository.count_daily()
    return DailyCountResponse(
        daily=[DailyCount(date=date, count=count) for date, count in counts]
    )


@users_router.get(
    path="/{user_id}",
    response_model=CreatedUser,
    status_code=status.HTTP_200_OK
)
async def get_user(
        user_id: str,
        user_repository: FromDishka[UserRepository]
) -> CreatedUser:
    user = await user_repository.get_by_user_id(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user


@users_router.patch(
    path="/",
    response_model=CreatedUser,
    status_code=status.HTTP_200_OK
)
async def set_user_id(
        phone_number: PhoneNumberQuery,
        update: UserUpdate,
        user_repository: FromDishka[UserRepository]
) -> CreatedUser:
    telegram_id = await user_repository.get_telegram_id_by_phone_number(phone_number)
    user = await user_repository.update(telegram_id, update.user_id)
    return user
