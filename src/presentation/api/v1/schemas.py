from typing import List

from pydantic import BaseModel

from src.core.entities import User, Contact


class UsersResponse(BaseModel):
    users: List[User]


class CountResponse(BaseModel):
    count: int


class ContactsResponse(BaseModel):
    contacts: List[Contact]
