from datetime import datetime

from pydantic import BaseModel


class ContactSchema(BaseModel):
    user_id: int
    phone_number: str
    created_at: [datetime]
