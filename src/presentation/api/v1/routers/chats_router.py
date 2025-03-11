from typing import Union

from fastapi import APIRouter, Query, status
from dishka.integrations.fastapi import FromDishka, DishkaRoute

from src.repository import DialogRepository
from src.controllers import ChatsController
from src.core.entities import ChatHistory, ChatHistoryPage
from src.schemas import DialogsResponse, DialogsCountResponse


chats_router = APIRouter(
    prefix="/api/v1/chats",
    tags=["Chats history"],
    route_class=DishkaRoute
)


@chats_router.get(
    path="/",
    response_model=DialogsResponse,
    status_code=status.HTTP_200_OK
)
async def get_dialogs(dialog_repository: FromDishka[DialogRepository]) -> DialogsResponse:
    dialogs = await dialog_repository.get_all()
    return DialogsResponse(dialogs=dialogs)


@chats_router.get(
    path="/{user_id}/",
    response_model=Union[ChatHistory, ChatHistoryPage],
    status_code=status.HTTP_200_OK
)
async def get_chat_history_by_user_id(
        user_id: int,
        chats_controller: FromDishka[ChatsController],
        is_paginated: bool = Query(default=False),
        page: int = Query(ge=1, default=1),
        limit: int = Query(ge=1, default=10),
) -> Union[ChatHistory, ChatHistoryPage]:
    chat_history = await chats_controller.get_chat_history(
        user_id=user_id,
        is_paginated=is_paginated,
        page=page,
        limit=limit
    )
    return chat_history


@chats_router.get(
    path="/count/",
    response_model=DialogsCountResponse,
    status_code=status.HTTP_200_OK
)
async def get_dialogs_count(dialog_repository: FromDishka[DialogRepository]) -> DialogsCountResponse:
    dialogs_count = await dialog_repository.get_total_count()
    return DialogsCountResponse(count=dialogs_count)


@chats_router.get(
    path="/{user_id}/count/",
    response_model=DialogsCountResponse,
    status_code=status.HTTP_200_OK
)
async def get_dialogs_count_by_user_id(
        user_id: int,
        dialog_repository: FromDishka[DialogRepository]
) -> DialogsCountResponse:
    dialogs_count = await dialog_repository.get_count_by_user_id(user_id)
    return DialogsCountResponse(count=dialogs_count)
