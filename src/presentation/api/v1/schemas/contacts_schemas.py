from typing import List

from pydantic import BaseModel

from src.core.entities import Contact


class ContactsResponse(BaseModel):
    contacts: List[Contact]


class ContactsCountResponse(BaseModel):
    count: int
