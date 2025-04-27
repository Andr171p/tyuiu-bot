from datetime import datetime

from typing import List, Tuple, Optional

from sqlalchemy import select, func
from sqlalchemy.ext.asyncio import AsyncSession

from src.core.entities import User
from src.core.interfaces import UserRepository
from src.infrastructure.database.models import UserModel


class SQLUserRepository(UserRepository):
    def __init__(self, session: AsyncSession) -> None:
        self._session = session

    async def create(self, user: User) -> int:
        self._session.add(UserModel(**user.model_dump()))
        await self._session.flush()
        id = user.id
        await self._session.commit()
        return id

    async def read(self, user_id: int) -> Optional[User]:
        stmt = (
            select(UserModel)
            .where(UserModel.user_id == user_id)
        )
        result = await self._session.execute(stmt)
        user = result.scalar_one_or_none()
        return User.model_validate(user) if user else None

    async def list(self) -> List[Optional[User]]:
        stmt = select(UserModel)
        results = await self._session.execute(stmt)
        users = results.scalars().all()
        return [User.model_validate(user) for user in users] if users else []

    async def paginate(self, page: int, limit: int) -> List[User]:
        offset = (page - 1) * limit
        stmt = (
            select(UserModel)
            .offset(offset)
            .limit(limit)
        )
        results = await self._session.execute(stmt)
        users = results.scalars().all()
        return [User.model_validate(user) for user in users] if users else []

    async def count(self) -> int:
        stmt = (
            select(func.count())
            .select_from(UserModel)
        )
        count = await self._session.execute(stmt)
        return count.scalar()

    async def count_daily(self) -> List[Tuple[datetime, int]]:
        stmt = (
            select(
                func.date(UserModel.created_at).label("date"),
                func.count().label("count")
            )
            .group_by(func.date(UserModel.created_at))
            .order_by(func.date(UserModel.created_at))
        )
        count = await self._session.execute(stmt)
        return list(count.scalars().all())
