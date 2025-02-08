from typing import List

from fastapi import APIRouter, status
from fastapi.responses import JSONResponse

from src.schemas import MessageSchema
from src.repository import MessageRepository
from src.utils.metrics import get_count, get_count_per_day


messages_router = APIRouter(
    prefix="/api/v1/messages",
    tags=["Messages"]
)


@messages_router.get(path="/{user_id}/", response_model=List[MessageSchema])
async def get_messages_by_user_id(user_id: int) -> JSONResponse:
    ...


@messages_router.get(path="/count/")
async def get_messages_count() -> JSONResponse:
    count = await get_count(MessageRepository())
    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content={"count": count}
    )
    
    
@messages_router.get(path="/count-per-day/")
async def get_messages_count_per_day() -> JSONResponse:
    count_per_day = await get_count_per_day(MessageRepository())
    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content={"count_per_day": count_per_day}
    )
