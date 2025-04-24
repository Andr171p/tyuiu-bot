from datetime import datetime

from typing import Optional

from pydantic import BaseModel


class User(BaseModel):
    user_id: int
    username: Optional[str]
    created_at: datetime

    class Config:
        from_attributes = True
