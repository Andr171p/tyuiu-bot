from datetime import datetime
from typing import List

from pydantic import BaseModel
from aiogram.types import Message


class ContactSchema(BaseModel):
    user_id: int
    phone_number: str
    created_at: datetime
    
    @classmethod
    def from_message(cls, message: Message) -> "ContactSchema":
        cls.user_id = message.from_user.id
        cls.phone_number = message.from_user.phone_number
        cls.created_at = datetime.now()
        
        
class SubscribersSchema(BaseModel):
    contacts: List[ContactSchema]
