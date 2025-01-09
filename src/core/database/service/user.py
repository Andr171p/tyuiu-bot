from src.core.database.models import User
from src.core.database.crud import CRUD


class UserService(CRUD):
    async def get_user_by_id(self, id: int) -> User | None:\
        return await self._read(id)

    async def add_user(self, user: User) -> User | None:
        db_user = await self._create(user)
        return db_user
