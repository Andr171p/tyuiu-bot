from datetime import datetime

from pydantic import BaseModel


class MessageSchema(BaseModel):
    question: str
    answer: str
    created_at: datetime
