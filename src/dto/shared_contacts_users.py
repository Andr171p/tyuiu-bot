from typing import List

from pydantic import BaseModel

from src.core.entities import Contact


class SharedContectUsers(BaseModel):
    contacts: List[Contact]
