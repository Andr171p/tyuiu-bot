from typing import List

from pydantic import BaseModel

from src.core.entities import Dialog


class DialogsResponse(BaseModel):
    dialogs: List[Dialog]


class DialogsCountResponse(BaseModel):
    count: int
