from typing import Sequence

from sqlalchemy import select

from src.database.models import User
from src.database.interfaces import BaseCRUD
from src.database.manager_provider import get_database_manager


class UserCRUD(BaseCRUD):
    def __init__(self, manager = get_database_manager()) -> None:
        self._manager = manager
        
    async def create(self, user: User) -> User | None:
        async with self._manager.session() as session:
            session.add(user)
            await session.commit()
        return user

    async def read_by_user_id(self, user_id: int) -> User | None:
        async with self._manager.session() as session:
            stmt = (
                select(User)
                .where(User.user_id == user_id)
            )
            user = await session.execute(stmt)
        return user.scalar_one_or_none()

    async def read_all(self) -> Sequence[User] | None:
        async with self._manager.session() as session:
            stmt = select(User)
            users = await session.execute(stmt)
        return users.scalars().all()
