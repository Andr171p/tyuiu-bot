from datetime import datetime 

from pydantic import BaseModel


class Dialog(BaseModel):
    user_id: int
    user_message: str
    chat_bot_message: str
    created_at: datetime
    
    class Config:
        from_attributes = True