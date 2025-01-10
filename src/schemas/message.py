from datetime import datetime

from pydantic import BaseModel


class MessageSchema(BaseModel):
    user_message: str
    bot_message: str
    created_at: datetime
