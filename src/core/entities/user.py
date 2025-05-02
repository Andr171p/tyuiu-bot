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
    first_name: Optional[str]
    last_name: Optional[str]
    username: Optional[str]
    user_id: Optional[str] = None
    phone_number: str
    created_at: datetime = Field(default_factory=datetime.now)

    model_config = ConfigDict(from_attributes=True)

    @field_validator("phone_number")
    @classmethod
    def format_phone_number(cls, phone_number: str) -> str:
        return format_phone_number(phone_number)


class ShareContactUser(BaseModel):
    telegram_id: int
    first_name: Optional[str]
    last_name: Optional[str]
    username: Optional[str]
    phone_number: str
