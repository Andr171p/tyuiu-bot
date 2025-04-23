from typing import Optional

from pydantic import BaseModel, field_validator

from src.utils import format_phone_number


class Notification(BaseModel):
    photo: Optional[bytes]
    text: str


class SubscriberNotification(Notification):
    phone_number: str

    @field_validator("phone_number")
    def validate_phone_number(self, phone_number: str) -> str:
        return format_phone_number(phone_number)
