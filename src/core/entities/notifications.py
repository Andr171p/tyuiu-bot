from io import BytesIO
from typing import Any

from pydantic import BaseModel, field_validator

from src.misc.formaters import format_phone_number


class NotificationAll(BaseModel):
    text: str


class NotificationAllWithPhoto(BaseModel):
    text: str
    photo: BytesIO


class NotificationByUserId(BaseModel):
    text: str
    user_id: int


class NotificationByPhoneNumber(BaseModel):
    text: str
    phone_number: str

    @field_validator("phone_number")
    def validate_phone_number(cls, phone_number: str) -> str:
        return format_phone_number(phone_number)


class NotificationWithPhotoByPhoneNumber(BaseModel):
    text: str
    photo: BytesIO
    phone_number: str

    @field_validator("phone_number")
    def validate_phone_number(cls, phone_number: str) -> str:
        return format_phone_number(phone_number)


class NotificationWithPhotoByUserId(BaseModel):
    text: str
    photo: Any
    user_id: int
