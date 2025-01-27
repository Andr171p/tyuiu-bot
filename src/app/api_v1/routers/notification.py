from fastapi import APIRouter, status
from fastapi.responses import JSONResponse

from dishka.integrations.fastapi import FromDishka, DishkaRoute

from src.app.bot import bot
from src.services import NotificationService
from src.app.api_v1.schemas import SendByPhoneNumberParams, SendAllParams


notification_router = APIRouter(
    prefix="/api/v1/notifications",
    route_class=DishkaRoute,
    tags=["Notification"]
)


@notification_router.post(path="/sendByPhoneNumber/")
async def send_notification(
        params: SendByPhoneNumberParams,
        notification_service: FromDishka[NotificationService]
) -> JSONResponse:
    await notification_service.send_notification_by_phone_number(
        phone_number=params.phone_number,
        text=params.text,
        bot=bot
    )
    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content={
            "status": "ok",
        }
    )


@notification_router.post(path="/sendAll/")
async def senf_notification_to_all_subscribers(
        params: SendAllParams,
        notification_service: FromDishka[NotificationService]
) -> JSONResponse:
    await notification_service.send_notification_to_all_subscribers(
        text=params.text,
        bot=bot
    )
    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content={
            "status": "ok",
        }
    )
