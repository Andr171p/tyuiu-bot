from fastapi import APIRouter, status
from fastapi.responses import JSONResponse

from src.repository import ContactRepository
from src.utils.metrics import get_count


subscribers_router = APIRouter(
    prefix="/api/v1/subscribers",
    tags=["Subscribers"]
)


@subscribers_router.get(path="/count/")
async def get_subscribers_count() -> JSONResponse:
    count = await get_count(ContactRepository())
    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content={"count": count}
    )
