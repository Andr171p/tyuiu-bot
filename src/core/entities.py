from typing import Literal, Optional

import uuid

from pydantic import BaseModel, ConfigDict, field_validator, model_validator

from ..utils import format_phone_number
from ..constants import USER_STATUSES, NOTIFICATION_TOPICS


class User(BaseModel):
    telegram_id: int
    user_id: Optional[uuid.UUID] = None
    first_name: Optional[str]
    last_name: Optional[str]
    username: Optional[str]
    phone_number: str
    status: USER_STATUSES = "READY"

    model_config = ConfigDict(from_attributes=True)

    @field_validator("phone_number")
    def format_phone_number(cls, phone_number: str) -> str:
        return format_phone_number(phone_number)

    @model_validator(mode="after")
    def set_status(self) -> "User":
        if self.user_id and self.phone_number:
            self.status = "READY"
        if not self.user_id and self.phone_number:
            self.status = "REGISTRATION_REQUIRE"
        return self


class Notification(BaseModel):
    notification_id: uuid.UUID
    topic: NOTIFICATION_TOPICS
    user_id: uuid.UUID
    phot: Optional[str] = None
    text: str

    model_config = ConfigDict(from_attributes=True)


class BaseMessage(BaseModel):
    role: Literal["user", "assistant"]
    chat_id: str | int
    text: str

    @field_validator("chat_id", mode="before")
    def validate_chat_id(cls, chat_id: str | int) -> str:
        return str(chat_id)


class UserMessage(BaseMessage):
    role: str = "user"


class AssistantMessage(BaseMessage):
    role: str = "assistant"
