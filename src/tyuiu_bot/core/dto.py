from typing import Optional, Union

from uuid import UUID
from datetime import datetime

from aiogram.types import ReplyKeyboardMarkup, InlineKeyboardMarkup

from pydantic import BaseModel, field_validator, model_validator

from ..utils import format_phone_number
from .entities import User, Notification
from ..constants import NOTIFICATION_STATUS, NOTIFICATION_LEVEL

from ..presentation.bot.keyboards import want_to_change_password_keyboard


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

    @field_validator("password", mode="before")
    def check_is_password_valid(cls, password: str) -> Optional[str]:
        ...

    @model_validator(mode="before")
    def check_confirm_password(self) -> "NewPasswordDTO":
        if self.new_password != self.confirmed_password:
            raise ValueError("Password not confirmed")
        return self


KEYBOARD = Union[ReplyKeyboardMarkup, InlineKeyboardMarkup]

LEVEL_TO_KEYBOARD: dict[NOTIFICATION_LEVEL: KEYBOARD] = {
    "CHANGE_PASSWORD": want_to_change_password_keyboard()
}
