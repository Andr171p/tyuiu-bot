from fastapi import APIRouter, status
from fastapi.responses import JSONResponse

from src.repository import (
    UserRepository,
    ContactRepository,
    MessageRepository
)
from src.utils.statistics import get_count, get_count_per_day


statistics_router = APIRouter(
    prefix="/api/v1/statistics"
)


@statistics_router.get(path="/getUsersCount/")
async def get_users_count() -> JSONResponse:
    users_count = await get_count(UserRepository())
    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content={
            "status": "ok",
            "count": users_count
        }
    )


@statistics_router.get(path="/getSubscribersCount/")
async def get_subscribers_count() -> JSONResponse:
    subscribers_count = await get_count(ContactRepository())
    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content={
            "status": "ok",
            "count": subscribers_count
        }
    )


@statistics_router.get(path="/getMessagesCountPerDay/")
async def get_messages_count_per_day() -> JSONResponse:
    message_count_per_day = await get_count_per_day(MessageRepository())
    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content={
            "status": "ok",
            "data": message_count_per_day
        }
    )


@statistics_router.get(path="/getUserCountPerDay/")
async def get_users_count_per_day() -> JSONResponse:
    users_count_per_day = await get_count_per_day(UserRepository())
    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content={
            "status": "ok",
            "data": users_count_per_day
        }
    )
