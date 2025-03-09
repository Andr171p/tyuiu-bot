from fastapi import APIRouter, status
from fastapi.responses import JSONResponse

from dishka.integrations.fastapi import FromDishka, DishkaRoute

from src.repository import UserRepository
from src.core.entities import User


users_router = APIRouter(
    prefix="/api/v1/users",
    tags=["Users"],
    route_class=DishkaRoute
)


@users_router.get(path="/", status_code=status.HTTP_200_OK)
async def get_users(user_repository: FromDishka[UserRepository]) -> JSONResponse:
    users = await user_repository.get_all()
    return JSONResponse(content={"users": users})


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
    path="/count/",
    status_code=status.HTTP_200_OK
)
async def get_users_count(user_repository: FromDishka[UserRepository]) -> JSONResponse:
    users_count = await user_repository.get_total_count()
    return JSONResponse(content={"count": users_count})