from typing import List, Optional

from src.dto import DateToCountDTO
from src.core.entities import User
from src.core.interfaces import AbstractRepository
from src.infrastructure.database.crud import UserCRUD
from src.infrastructure.database.models import UserModel


class UserRepository(AbstractRepository):
    def __init__(self, crud: UserCRUD) -> None:
        self._crud = crud

    async def save(self, user: User) -> int:
        return await self._crud.create(UserModel(**user.model_dump()))

    async def get(self, user_id: int) -> Optional[User]:
        user = await self._crud.read(user_id)
        return User.model_validate(user) if user else None

    async def list(self) -> List[Optional[User]]:
        users = await self._crud.read_all()
        return [User.model_validate(user) for user in users] if users else []

    async def count(self) -> int:
        return await self._crud.read_total_count()

    async def date_to_count(self) -> List[DateToCountDTO]:
        date_to_count = await self._crud.read_date_to_count()
        return [
            DateToCountDTO(date=date, count=count)
            for date, count in date_to_count
        ]
