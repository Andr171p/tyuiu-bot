from typing import Optional

from datetime import datetime
from uuid import UUID

from pydantic import BaseModel, field_validator

from .entities import User, Notification
from ..constants import NOTIFICATION_STATUSES
from ..utils import format_phone_number


class UserReadDTO(User):
    created_at: datetime
    updated_at: datetime


class UserContactDTO(BaseModel):
    telegram_id: int
    first_name: Optional[str]
    last_name: Optional[str]
    username: Optional[str]
    phone_number: str

    @field_validator("phone_number")
    def format_phone_number(cls, phone_number: str) -> str:
        return format_phone_number(phone_number)


class NotificationCreateDTO(Notification):
    status: NOTIFICATION_STATUSES
    message_id: Optional[int]


class NotificationReadDTO(Notification):
    notification_id: UUID
    status: NOTIFICATION_STATUSES
    created_at: datetime
