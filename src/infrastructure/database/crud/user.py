from datetime import datetime

from typing import Sequence, Tuple, Optional

from sqlalchemy import select, func
from sqlalchemy.ext.asyncio import AsyncSession

from src.infrastructure.database.crud.base import CRUD
from src.infrastructure.database.models import UserModel


class UserCRUD(CRUD):
    def __init__(self, session: AsyncSession) -> None:
        self._session = session

    async def create(self, user: UserModel) -> int:
        self._session.add(user)
        await self._session.flush()
        id = user.id
        await self._session.commit()
        return id

    async def read(self, user_id: int) -> Optional[UserModel]:
        stmt = (
            select(UserModel)
            .where(UserModel.user_id == user_id)
        )
        user = await self._session.execute(stmt)
        return user.scalar_one_or_none()

    async def read_all(self) -> Sequence[UserModel]:
        stmt = select(UserModel)
        users = await self._session.execute(stmt)
        return users.scalars().all()

    async def count(self) -> int:
        stmt = (
            select(func.count())
            .select_from(UserModel)
        )
        total_count = await self._session.execute(stmt)
        return total_count.scalar_one_or_none()

    async def read_count_by_creation_date(self) -> Sequence[Tuple[datetime, int]]:
        stmt = (
            select(
                func.date(UserModel.created_at).label("date"),
                func.count().label("count")
            )
            .group_by(func.date(UserModel.created_at))
            .order_by(func.date(UserModel.created_at))
        )
        date_to_count = await self._session.execute(stmt)
        return date_to_count.scalars().all()
