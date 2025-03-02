from typing import List

from pydantic import BaseModel

from src.core.entities import Chat


class ChatHistory(BaseModel):
    user_id: int
    chats: List[Chat]
