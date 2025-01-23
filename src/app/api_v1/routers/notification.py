from fastapi import APIRouter, status
from fastapi.responses import JSONResponse

from dishka.integrations.fastapi import FromDishka, DishkaRoute

from src.app.bot import bot
from src.services import NotificationService


notification_router = APIRouter(
    prefix="/api/v1/notifications",
    route_class=DishkaRoute
)


@notification_router.post(path="/sendByPhoneNumber/")
async def send_notification(
        phone_number: str,
        text: str,
        notification_service: FromDishka[NotificationService]
) -> JSONResponse:
    await notification_service.send_notification_by_phone_number(
        phone_number=phone_number,
        text=text,
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
        text: str,
        notification_service: FromDishka[NotificationService]
) -> JSONResponse:
    await notification_service.send_notification_to_all_subscribers(
        text=text,
        bot=bot
    )
    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content={
            "status": "ok",
        }
    )
