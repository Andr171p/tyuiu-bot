from typing import Optional, List

from pydantic import BaseModel, field_validator

from src.utils import format_phone_number


class Recipient(BaseModel):
    phone_number: str

    @field_validator("phone_number")
    def validate_phone_number(cls, phone_number: str) -> str:
        return format_phone_number(phone_number)


class Message(BaseModel):
    text: str
    image_url: Optional[str] = None
    image_base64: Optional[str] = None


class GlobalNotification(BaseModel):
    message: Message


class BroadcastNotification(BaseModel):
    message: Message
    recipients: List[Recipient]


class DirectNotification(BaseModel):
    message: Message
    recipient: Recipient
