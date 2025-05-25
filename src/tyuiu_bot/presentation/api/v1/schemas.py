from typing import Annotated

from uuid import UUID

from pydantic import BaseModel

from fastapi import Query, Form

from src.tyuiu_bot.core.dto import NotificationReadDTO


PhoneNumberQuery = Annotated[
    str,
    Query(..., description="Номер телефона для поиска в формате +7(XXX)XXX-XX-XX")
]

UserIdUpdate = Annotated[
    UUID,
    Form(..., description="Id пользователя в сервисе регистрации")
]


class UserNotificationsResponse(BaseModel):
    notifications: list[NotificationReadDTO]
