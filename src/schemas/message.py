from datetime import datetime
from typing import List

from pydantic import BaseModel


class MessageSchema(BaseModel):
    user_id: int
    user_message: str
    bot_message: str
    created_at: datetime
    
    
class PaginatedMessagesSchema(BaseModel):
    user_id: int
    total: int
    page: int
    limit: int
    messages: List[MessageSchema]
