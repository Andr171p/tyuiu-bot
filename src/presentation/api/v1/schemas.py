from datetime import datetime

from typing import Annotated, List

from fastapi import Query
from pydantic import BaseModel

from src.core.entities import User


PhoneNumberQuery = Annotated[
    str,
    Query(..., description="Номер телефона для поиска в формате +7(xxx)xxx-xx-xx")
]


class UsersResponse(BaseModel):
    users: List[User]


class UsersPageResponse(BaseModel):
    total: int
    page: int
    limit: int
    users: List[User]


class UserIdUpdate(BaseModel):
    user_id: str


class CountResponse(BaseModel):
    count: int


class DailyCount(BaseModel):
    date: datetime
    count: int


class DailyCountResponse(BaseModel):
    daily: List[DailyCount]
