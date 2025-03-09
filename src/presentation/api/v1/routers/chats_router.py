from fastapi import APIRouter, Query, status
from fastapi.responses import JSONResponse

from dishka.integrations.fastapi import FromDishka, DishkaRoute

from src.repository import DialogRepository
from src.core.use_cases import UsersUseCase
from src.core.entities import ChatHistory, ChatHistoryPage


chats_router = APIRouter(
    prefix="/api/v1/chats",
    tags=["Chats history"],
    route_class=DishkaRoute
)


@chats_router.get(path="/", status_code=status.HTTP_200_OK)
async def get_dialogs(dialog_repository: FromDishka[DialogRepository]) -> JSONResponse:
    dialogs = await dialog_repository.get_all()
    return JSONResponse(content={"dialogs": dialogs})


@chats_router.get(
    path="/{user_id}/",
    response_model=ChatHistory,
    status_code=status.HTTP_200_OK
)
async def get_chat_history_by_user_id(
        user_id: int,
        users_use_case: FromDishka[UsersUseCase]
) -> ChatHistory:
    chat_history = await users_use_case.get_chat_history(user_id)
    return chat_history


@chats_router.get(
    path="/{user_id}/",
    response_model=ChatHistoryPage,
    status_code=status.HTTP_200_OK
)
async def get_chat_history_page_by_user_id(
        user_id: int,
        users_use_case: FromDishka[UsersUseCase],
        page: int = Query(ge=1, default=1),
        limit: int = Query(ge=1, le=100, default=10),
) -> ChatHistoryPage:
    chat_history_page = await users_use_case.get_page_of_chat_history(
        user_id=user_id,
        page=page,
        limit=limit
    )
    return chat_history_page


@chats_router.get(
    path="/count",
    status_code=status.HTTP_200_OK
)
async def get_dialogs_count(dialog_repository: FromDishka[DialogRepository]) -> JSONResponse:
    dialogs_count = await dialog_repository.get_total_count()
    return JSONResponse(content={"count": dialogs_count})


@chats_router.get(
    path="/{user_id}/count/",
    status_code=status.HTTP_200_OK
)
async def get_dialogs_count_by_user_id(
        user_id: int,
        dialog_repository: FromDishka[DialogRepository]
) -> JSONResponse:
    dialogs_count = await dialog_repository.get_count_by_user_id(user_id)
    return JSONResponse(content={"count": dialogs_count})
