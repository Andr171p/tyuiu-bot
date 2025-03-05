from fastapi import APIRouter, status
from fastapi.responses import JSONResponse

from dishka.integrations.fastapi import FromDishka, DishkaRoute

from src.core.use_cases import ChatsUseCase
from src.core.entities import Chat
from src.dto import ChatPaginated


chats_router = APIRouter(
    prefix="/api/v1/chats",
    tags=["Chats"],
    route_class=DishkaRoute
)


@chats_router.get(path="/{user_id}/", response_model=Chat)
async def get_chat_history_by_user_id(
        user_id: int,
        chats: FromDishka[ChatsUseCase]
) -> JSONResponse:
    chat = await chats.get_history_by_user_id(user_id)
    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content=chat.model_dump()
    )


@chats_router.get(path="/{user_id}/page={page}/limit={limit}", response_model=ChatPaginated)
async def get_chat_history_paginated_by_user_id(
        user_id: int,
        page: int,
        limit: int,
        chats: FromDishka[ChatsUseCase]
) -> JSONResponse:
    chat_page = await chats.get_paginated_history_by_user_id(
        user_id=user_id,
        page=page,
        limit=limit
    )
    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content=chat_page.model_dump()
    )


@chats_router.get(path="/count/")
async def get_dialogs_count(chats: FromDishka[ChatsUseCase]) -> JSONResponse:
    dialogs_count = await chats.get_total_dialogs_count()
    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content={"count": dialogs_count}
    )


@chats_router.get(path="/{user_id}/count/")
async def get_dialogs_count_by_user_id(
        user_id: int,
        chats: FromDishka[ChatsUseCase]
) -> JSONResponse:
    dialogs_count = await chats.get_dialogs_count_by_user_id(user_id)
    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content={"count": dialogs_count}
    )


@chats_router.get(path="/")
async def get_chats(chats: FromDishka[ChatsUseCase]) -> JSONResponse:
    dialogs = await chats.get_dialogs_history()
    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content={"dialogs": [dialog.model_dump() for dialog in dialogs]}
    )
