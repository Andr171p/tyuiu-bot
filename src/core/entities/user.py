from enum import Enum, auto
from datetime import datetime

from typing import Optional

from pydantic import (
    BaseModel,
    field_validator,
    ConfigDict,
    Field
)

from src.utils import format_phone_number


class User(BaseModel):
    telegram_id: int
    user_id: Optional[str] = None
    username: Optional[str]
    phone_number: Optional[str] = None
    created_at: datetime = Field(default_factory=datetime.now)

    model_config = ConfigDict(from_attributes=True)

    @field_validator("phone_number")
    @classmethod
    def format_phone_number(cls, phone_number: str) -> str:
        return format_phone_number(phone_number)


class UserShareContact(BaseModel):
    telegram_id: int
    user_id: Optional[str] = None
    phone_number: str

    @field_validator("phone_number")
    @classmethod
    def format_phone_number(cls, phone_number: str) -> str:
        return format_phone_number(phone_number)


class SharingContactStatus(Enum):
    SUCCESS = auto()  # contact created and user registered
    ALREADY_SHARED = auto()  # contact already created and user registered
    NOT_REGISTERED = auto()  # contact created and user not registered
    ERROR = auto()  # error while create contact
