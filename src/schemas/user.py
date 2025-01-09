from datetime import datetime

from pydantic import BaseModel


class UserSchema(BaseModel):
    user_id: int
    username: str | None
    created_at: datetime
