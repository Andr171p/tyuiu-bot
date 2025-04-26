from typing import Optional, List

from pydantic import BaseModel, field_validator

from src.utils import format_phone_number


class Recipient(BaseModel):
    phone_number: str

    @field_validator("phone_number")
    def validate_phone_number(cls, phone_number: str) -> str:
        return format_phone_number(phone_number)


class NotificationContent(BaseModel):
    text: str
    photo_url: Optional[str] = None
    photo_base64: Optional[str] = None


class PublicNotification(BaseModel):
    content: NotificationContent


class DirectedNotification(BaseModel):
    recipients: List[Recipient]
    content: NotificationContent
