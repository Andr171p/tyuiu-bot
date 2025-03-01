from typing import TYPE_CHECKING, Sequence

from sqlalchemy import select

if TYPE_CHECKING:
    from src.db.database_manager import DatabaseManager

from src.db.crud.base_crud import BaseCRUD
from src.db.models import UserModel


class UserCRUD(BaseCRUD):
    def __init__(self, manager: "DatabaseManager") -> None:
        self._manager = manager
        
    async def create(self, user: UserModel) -> int:
        async with self._manager.session() as session:
            session.add(user)
            await session.commit()
            id = user.id
        return id
    
    async def read_by_user_id(self, user_id: int) -> UserModel | None:
        async with self._manager.session() as session:
            stmt = (
                select(UserModel)
                .where(UserModel.user_id == user_id)
            )
            user = await session.execute(stmt)
        return user.scalar_one_or_none()
    
    async def read_all(self) -> Sequence[UserModel] | None:
        async with self._manager.session() as session:
            stmt = select(UserModel)
            users = await session.execute(stmt)
        return users.scalars().all()
