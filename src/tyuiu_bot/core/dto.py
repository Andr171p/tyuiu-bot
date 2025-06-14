from typing import Optional

from uuid import UUID
from datetime import datetime

from pydantic import BaseModel, field_validator, model_validator

from .entities import User, Notification
from .exceptions import ConfirmedPasswordError

from ..utils import format_phone_number
from ..constants import NOTIFICATION_STATUS


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
    status: NOTIFICATION_STATUS
    message_id: Optional[int]


class NotificationReadDTO(Notification):
    notification_id: UUID
    status: NOTIFICATION_STATUS
    created_at: datetime


class SentNotificationDTO(BaseModel):
    notification_id: UUID
    sent_at: datetime


class NewPasswordDTO(BaseModel):
    telegram_id: int
    new_password: str
    confirmed_password: str

    @model_validator(mode="before")
    def check_confirm_password(self) -> "NewPasswordDTO":
        if self.new_password != self.confirmed_password:
            raise ConfirmedPasswordError("Password not confirmed")
        return self
