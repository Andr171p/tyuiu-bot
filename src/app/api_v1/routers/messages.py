from fastapi import APIRouter, status
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder

from dishka.integrations.fastapi import FromDishka, DishkaRoute

from src.schemas import (
    MessageSchema, 
    MessagesHistorySchema,
    PaginatedMessagesSchema
)
from src.repository import MessageRepository
from src.services import ChatService
from src.utils.metrics import get_count, get_count_per_day


messages_router = APIRouter(
    prefix="/api/v1/messages",
    tags=["Messages"],
    route_class=DishkaRoute
)


@messages_router.get(path="/{user_id}/", response_model=MessagesHistorySchema)
async def get_messages_history_by_user_id(
    user_id: int,
    chat_service: FromDishka[ChatService]
) -> JSONResponse:
    messages_history = await chat_service.get_messages_history_by_user_id(user_id)
    json_messages_history = jsonable_encoder(messages_history)
    return JSONResponse( 
        status_code=status.HTTP_200_OK,
        content=json_messages_history
    )
    
    
@messages_router.get(
    path="/{user_id}/?page={page}", 
    response_model=PaginatedMessagesSchema
)
async def get_paginated_messages_by_user_id(
    user_id: int,
    page: int,
    chat_service: FromDishka[ChatService],
) -> JSONResponse:
    paginated_messages = await chat_service.get_paginated_messages_history_by_user_id(
        user_id=user_id,
        page=page
    )
    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content=paginated_messages.model_dump()
    )


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
