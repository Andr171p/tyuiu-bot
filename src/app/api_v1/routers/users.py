from fastapi import APIRouter, status
from fastapi.responses import JSONResponse

from src.repository import UserRepository
from src.utils.metrics import get_count, get_count_per_day


users_router = APIRouter(
    prefix="/api/v1/users",
    tags=["Users"]
)


@users_router.get(path="/count/")
async def get_users_count() -> JSONResponse:
    count = await get_count(UserRepository())
    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content={"count": count}
    )
    
    
@users_router.get(path="/count-per-day/")
async def get_users_count_per_day() -> JSONResponse:
    count_per_day = await get_count_per_day(UserRepository())
    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content={"count_per_day": count_per_day}
    )
