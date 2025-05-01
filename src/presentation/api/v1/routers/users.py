from typing import Union

from fastapi import (
    APIRouter,
    status,
    Query,
    HTTPException,
    BackgroundTasks
)
from dishka.integrations.fastapi import FromDishka, DishkaRoute

from faststream.rabbit import RabbitBroker

from src.core.entities import User, NotificationOne, Content
from src.core.interfaces import UserRepository
from ..schemas import (
    PhoneNumberQuery,
    UsersResponse,
    UsersPageResponse,
    UserIdUpdate,
    CountResponse,
    DailyCount,
    DailyCountResponse
)
from src.constants import (
    GE_PAGINATED,
    DEFAULT_PAGE,
    DEFAULT_LIMIT,
    DEFAULT_IS_PAGINATED
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
        is_paginated: bool = Query(default=DEFAULT_IS_PAGINATED),
        page: int = Query(ge=GE_PAGINATED, default=DEFAULT_PAGE),
        limit: int = Query(ge=GE_PAGINATED, default=DEFAULT_LIMIT)
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
    path="/{telegram_id}",
    response_model=User,
    status_code=status.HTTP_200_OK
)
async def get_user(
        telegram_id: int,
        user_repository: FromDishka[UserRepository]
) -> User:
    user = await user_repository.read(telegram_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user


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
    path="/shared-contacts/",
    response_model=Union[UsersResponse, UsersPageResponse],
    status_code=status.HTTP_200_OK
)
async def get_shared_contact_users(
        user_repository: FromDishka[UserRepository],
        is_paginated: bool = Query(default=DEFAULT_IS_PAGINATED),
        page: int = Query(ge=GE_PAGINATED, default=DEFAULT_PAGE),
        limit: int = Query(ge=GE_PAGINATED, default=DEFAULT_LIMIT)
) -> Union[UsersResponse, UsersPageResponse]:
    if is_paginated:
        total = await user_repository.count_registered()
        users = await user_repository.paginate_registered(page, limit)
        return UsersPageResponse(
            total=total,
            page=page,
            limit=limit,
            users=users
        )
    users = await user_repository.list_registered()
    return UsersResponse(users=users)


@users_router.get(
    path="/shared-contacts/{user_id}",
    response_model=Union,
    status_code=status.HTTP_200_OK
)
async def get_shared_contact_user(user_id: str, user_repository: FromDishka[UserRepository]) -> User:
    user = await user_repository.get_by_user_id(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User has not yet shared the contact")
    return user


@users_router.patch(
    path="/shared-contacts",
    response_model=User,
    status_code=status.HTTP_200_OK
)
async def add_user_id(
        phone_number: PhoneNumberQuery,
        user: UserIdUpdate,
        user_repository: FromDishka[UserRepository],
        broker: FromDishka[RabbitBroker],
        background_tasks: BackgroundTasks
) -> User:
    telegram_id = await user_repository.get_telegram_id_by_phone_number(phone_number)
    if not telegram_id:
        raise HTTPException(status_code=404, detail=f"User with not created yet")
    user = await user_repository.update(telegram_id, user_id=user.user_id)
    notification = NotificationOne(
        phone_number=phone_number,
        content=Content(text="Вы успешно зарегистрированы и готовы получать уведомления")
    )
    background_tasks.add_task(
        broker.publish,
        notification,
        queue="chat.tasks.messages",
    )
    return user
