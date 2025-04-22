from typing import List, Optional

from src.infrastructure.database.models import UserModel
from src.infrastructure.database.crud import UserCRUD
from src.core.interfaces import AbstractRepository
from src.core.entities import User


class UserRepository(AbstractRepository):
    def __init__(self, crud: UserCRUD) -> None:
        self._crud = crud

    async def save(self, user: User) -> int:
        return await self._crud.create(UserModel(**user.model_dump()))
    
    async def get(self, user_id: int) -> Optional[User]:
        user = await self._crud.read_by_user_id(user_id)
        return User.model_validate(user) if user else None
    
    async def list(self) -> List[Optional[User]]:
        users = await self._crud.read_all()
        return [User.model_validate(user) for user in users] if users else []
    
    async def total_count(self) -> int:
        return await self._crud.read_total_count()
