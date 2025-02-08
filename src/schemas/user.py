from datetime import datetime

from pydantic import BaseModel
from aiogram.types import Message


class UserSchema(BaseModel):
    user_id: int
    username: str | None
    created_at: datetime
    
    @classmethod
    def from_message(cls, message: Message) -> "UserSchema":
        cls.user_id = message.from_user.id
        cls.username = message.from_user.username
        cls.created_at = datetime.now()
