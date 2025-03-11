from typing import List

from pydantic import BaseModel

from src.core.entities.dialog import Dialog


class ChatHistory(BaseModel):
    user_id: int
    dialogs: List[Dialog]


class ChatHistoryPage(BaseModel):
    user_id: int
    total: int
    page: int
    limit: int
    dialogs: List[Dialog]
