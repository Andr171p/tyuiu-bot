from typing import Annotated

from uuid import UUID

from pydantic import BaseModel

from fastapi import Query, Form

from src.core.dto import NotificationReadDTO


PhoneNumberQuery = Annotated[
    str,
    Query(..., description="Номер телефона для поиска в формате +7(xxx)xxx-xx-xx")
]

UserIdUpdate = Annotated[
    UUID,
    Form(..., description="Id пользователя в сервисе регистрации")
]


class CreatedNotificationResponse(BaseModel):
    notification_id: UUID


class UserNotificationsResponse(BaseModel):
    user_id: UUID
    notifications: list[NotificationReadDTO]
