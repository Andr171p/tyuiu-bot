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
        return cls(
            user_id=message.from_user.id,
            phone_number=message.contact.phone_number,
            created_at=datetime.now()
        )
        
        
class SubscribersSchema(BaseModel):
    contacts: List[ContactSchema]
