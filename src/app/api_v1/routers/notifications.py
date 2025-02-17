from typing import List

from fastapi import APIRouter, status
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder

from dishka.integrations.fastapi import FromDishka, DishkaRoute

from src.app.bot import bot
from src.services import NotificationService
from src.schemas import (
    NotifyByPhoneNumberSchema, 
    NotifyAllSchema, 
    ContactSchema
)


notifications_router = APIRouter(
    prefix="/api/v1/notifications",
    route_class=DishkaRoute,
    tags=["Notification"]
)


@notifications_router.post(path="/", response_model=ContactSchema)
async def notify_by_phone_number(
        params: NotifyByPhoneNumberSchema,
        notification_service: FromDishka[NotificationService]
) -> JSONResponse:
    contact = await notification_service.notify_by_phone_number(
        phone_number=params.phone_number,
        text=params.text,
        bot=bot
    )
    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content=jsonable_encoder(contact)
    )


@notifications_router.post(path="/all/", response_model=List[ContactSchema])
async def notify_all_subscribers(
        params: NotifyAllSchema,
        notification_service: FromDishka[NotificationService]
) -> JSONResponse:
    contacts = await notification_service.notify_all_subscribers(
        text=params.text,
        bot=bot
    )
    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content=jsonable_encoder(contacts)
    )
