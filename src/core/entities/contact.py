from datetime import datetime

from pydantic import BaseModel, field_validator

from src.utils import format_phone_number


class Contact(BaseModel):
    user_id: int
    phone_number: str
    is_exists: str
    created_at: datetime
    
    class Config:
        from_attributes = True

    @field_validator("phone_number")
    def validate_phone_number(cls, phone_number: str) -> str:
        return format_phone_number(phone_number)
    