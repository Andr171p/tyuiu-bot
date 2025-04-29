from enum import Enum, auto
from datetime import datetime

from typing import Optional

from pydantic import BaseModel, field_validator

from src.utils import format_phone_number


class User(BaseModel):
    telegram_id: int
    user_id: Optional[str] = None
    username: Optional[str]

    class Config:
        from_attributes = True


class Contact(BaseModel):
    telegram_id: int
    phone_number: str
    is_registered: bool

    class Config:
        from_attributes = True

    @field_validator("phone_number")
    def format_phone_number(cls, phone_number: str) -> str:
        return format_phone_number(phone_number)


class SharingContactStatus(Enum):
    SUCCESS = auto()  # contact created and user registered
    ALREADY_SHARED = auto()  # contact already created and user registered
    NOT_REGISTERED = auto()  # contact created and user not registered
    ERROR = auto()  # error while create contact


class CreatedUser(User):
    created_at: datetime


class CreatedContact(Contact):
    created_at: datetime
