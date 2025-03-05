from typing import List

from pydantic import BaseModel

from src.core.entities.dialog import Dialog


class Chat(BaseModel):
    user_id: int
    dialogs: List[Dialog]
