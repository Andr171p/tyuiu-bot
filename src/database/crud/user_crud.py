from typing import TYPE_CHECKING, Sequence, List, Tuple
from datetime import datetime

from sqlalchemy import select, func

if TYPE_CHECKING:
    from src.database.database_manager import DatabaseManager

from src.database.crud.base_crud import BaseCRUD
from src.database.models import UserModel


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
    
    async def read_total_count(self) -> int | None:
        async with self._manager.session() as session:
            stmt = (
                select(func.count())
                .select_from(UserModel)
            )
            users_count = await session.execute(stmt)
        return users_count.scalar_one_or_none()

    async def read_count_per_day(self) -> List[Tuple[datetime, int]]:
        async with self._manager.session() as session:
            stmt = (
                select(
                    func.date(UserModel.created_at).label("date"),
                    func.count().label("count")
                )
                .group_by(func.date(UserModel.created_at))
                .order_by(func.date(UserModel.created_at))
            )
            counts_per_days = await session.execute(stmt)
        return counts_per_days.all()
