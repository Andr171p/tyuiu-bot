from datetime import datetime

from typing import Annotated, List

from fastapi import Query
from pydantic import BaseModel

from src.core.entities import User, Contact


PhoneNumberQuery = Annotated[
    str,
    Query(..., description="Номер телефона для поиска в формате +7(xxx)xxx-xx-xx")
]


class UsersResponse(BaseModel):
    users: List[User]


class CountResponse(BaseModel):
    count: int


class ContactsResponse(BaseModel):
    contacts: List[Contact]


class ContactUpdate(BaseModel):
    is_exists: bool


class DailyCount(BaseModel):
    date: datetime
    count: int


class DailyCountResponse(BaseModel):
    distribution: List[DailyCount]


class SentNotificationResponse(BaseModel):
    detail: str = "Notification sent successfully"
