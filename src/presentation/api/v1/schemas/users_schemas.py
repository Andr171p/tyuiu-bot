from typing import List

from pydantic import BaseModel

from src.core.entities import User


class UsersResponse(BaseModel):
    users: List[User]


class UsersCountResponse(BaseModel):
    count: int
