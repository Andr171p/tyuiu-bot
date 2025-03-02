from typing import List

from pydantic import BaseModel

from src.core.entities import Dialog


class DialogsHistory(BaseModel):
    user_id: int
    dialogs: List[Dialog]
