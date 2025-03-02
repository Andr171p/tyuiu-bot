from typing import List

from pydantic import BaseModel

from src.core.entities import Dialog


class PaginatedDialogs(BaseModel):
    user_id: int
    total: int
    page: int
    limit: int
    dialogs: List[Dialog]
    