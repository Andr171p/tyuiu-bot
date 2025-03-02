from typing import List

from pydantic import BaseModel

from src.core.entities import Chat


class ChatHistoryPaginated(BaseModel):
    user_id: int
    total: int
    page: int
    limit: int
    chats: List[Chat]
    