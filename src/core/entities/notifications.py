from typing import Any

from pydantic import BaseModel


class NotificationAll(BaseModel):
    text: str


class NotificationAllWithPhoto(BaseModel):
    text: str
    photo: Any


class NotificationByUserId(BaseModel):
    text: str
    user_id: int


class NotificationByPhoneNumber(BaseModel):
    text: str
    phone_number: str


class NotificationWithPhotoByPhoneNumber(BaseModel):
    text: str
    photo: Any
    phone_number: str


class NotificationWithPhotoByUserId(BaseModel):
    text: str
    photo: Any
    user_id: int
