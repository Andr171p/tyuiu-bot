from fastapi import APIRouter, status
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder

from dishka.integrations.fastapi import FromDishka, DishkaRoute

from src.schemas import SubscribersSchema
from src.repository import ContactRepository
from src.services import NotificationService
from src.utils.metrics import get_count


subscribers_router = APIRouter(
    prefix="/api/v1/subscribers",
    tags=["Subscribers"],
    route_class=DishkaRoute
)


@subscribers_router.get("/", response_model=SubscribersSchema)
async def get_all_subscribers(
    notification_service: FromDishka[NotificationService]
) -> JSONResponse:
    subscribers = await notification_service.get_all_subscribers()
    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content=jsonable_encoder(subscribers)
    )


@subscribers_router.get(path="/count/")
async def get_subscribers_count() -> JSONResponse:
    count = await get_count(ContactRepository())
    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content={"count": count}
    )
