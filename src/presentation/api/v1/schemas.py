from datetime import datetime

from typing import Annotated, List

from fastapi import Query
from pydantic import BaseModel

from src.core.entities import CreatedUser, CreatedContact


PhoneNumberQuery = Annotated[
    str,
    Query(..., description="Номер телефона для поиска в формате +7(xxx)xxx-xx-xx")
]


class UsersResponse(BaseModel):
    users: List[CreatedUser]


class UsersPageResponse(BaseModel):
    total: int
    page: int
    limit: int
    users: List[CreatedUser]


class UserUpdate(BaseModel):
    user_id: str


class CountResponse(BaseModel):
    count: int


class ContactsResponse(BaseModel):
    contacts: List[CreatedContact]


class ContactsPageResponse(BaseModel):
    total: int
    page: int
    limit: int
    contacts: List[CreatedContact]


class DailyCount(BaseModel):
    date: datetime
    count: int


class DailyCountResponse(BaseModel):
    daily: List[DailyCount]
