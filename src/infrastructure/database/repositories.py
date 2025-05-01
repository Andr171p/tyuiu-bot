from datetime import datetime

from typing import List, Tuple, Optional, Sequence

from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy import select, update, func
from sqlalchemy.ext.asyncio import AsyncSession

from .models import UserModel
from src.core.interfaces import UserRepository
from src.core.entities import User


class SQLUserRepository(UserRepository):
    def __init__(self, session: AsyncSession) -> None:
        self.session = session

    async def create(self, user: User) -> User:
        try:
            user_model = UserModel.from_user(user)
            self.session.add(user_model)
            await self.session.flush()
            await self.session.commit()
            return User.model_validate(user_model)
        except SQLAlchemyError as ex:
            await self.session.rollback()
            raise RuntimeError(f"Error while creating user: {ex}")

    async def read(self, telegram_id: int) -> Optional[User]:
        try:
            stmt = (
                select(UserModel)
                .where(UserModel.telegram_id == telegram_id)
            )
            result = await self.session.execute(stmt)
            user = result.scalar_one_or_none()
            return User.model_validate(user) if user else None
        except SQLAlchemyError as ex:
            await self.session.rollback()
            raise RuntimeError(f"Error while reading user: {ex}")

    async def update(self, telegram_id: int, **kwargs) -> User:
        try:
            stmt = (
                update(UserModel)
                .where(UserModel.telegram_id == telegram_id)
                .values(**kwargs)
                .returning(UserModel)
            )
            result = await self.session.execute(stmt)
            user = result.scalar_one()
            await self.session.commit()
            return User.model_validate(user)
        except SQLAlchemyError as ex:
            await self.session.rollback()
            raise RuntimeError(f"Error while update user: {ex}")

    async def list(self) -> List[User]:
        try:
            stmt = select(UserModel)
            results = await self.session.execute(stmt)
            users = results.scalars().all()
            return [User.model_validate(user) for user in users] if users else []
        except SQLAlchemyError as ex:
            await self.session.rollback()
            raise RuntimeError(f"Error while reding users: {ex}")

    async def list_registered(self) -> List[User]:
        try:
            stmt = (
                select(UserModel)
                .where(UserModel.user_id is not None)
            )
            results = await self.session.execute(stmt)
            users = results.scalars().all()
            return [User.model_validate(user) for user in users] if users else []
        except SQLAlchemyError as ex:
            await self.session.rollback()
            raise RuntimeError(f"Error while reding users: {ex}")

    async def paginate(self, page: int, limit: int) -> List[User]:
        try:
            offset = (page - 1) * limit
            stmt = (
                select(UserModel)
                .offset(offset)
                .limit(limit)
            )
            results = await self.session.execute(stmt)
            users = results.scalars().all()
            return [User.model_validate(user) for user in users] if users else []
        except SQLAlchemyError as ex:
            await self.session.rollback()
            raise RuntimeError(f"Error while reading paginated users: {ex}")

    async def paginate_registered(self, page: int, limit: int) -> List[User]:
        try:
            offset = (page - 1) * limit
            stmt = (
                select(UserModel)
                .where(UserModel.user_id is not None)
                .offset(offset)
                .limit(limit)
            )
            results = await self.session.execute(stmt)
            users = results.scalars().all()
            return [User.model_validate(user) for user in users] if users else []
        except SQLAlchemyError as ex:
            await self.session.rollback()
            raise RuntimeError(f"Error while reading paginated users: {ex}")

    async def get_by_user_id(self, user_id: str) -> Optional[User]:
        try:
            stmt = (
                select(UserModel)
                .where(UserModel.user_id == user_id)
            )
            result = await self.session.execute(stmt)
            user = result.scalar_one_or_none()
            return User.model_validate(user) if user else None
        except SQLAlchemyError as ex:
            await self.session.rollback()
            raise RuntimeError(f"Error while reading user: {ex}")

    async def get_by_phone_number(self, phone_number: str) -> Optional[User]:
        try:
            stmt = (
                select(UserModel)
                .where(UserModel.phone_number == phone_number)
            )
            result = await self.session.execute(stmt)
            user = result.scalar_one_or_none()
            return User.model_validate(user) if user else None
        except SQLAlchemyError as ex:
            await self.session.rollback()
            raise RuntimeError(f"Error while reading user: {ex}")

    async def get_telegram_id_by_user_id(self, user_id: str) -> int:
        try:
            stmt = (
                select(UserModel.telegram_id)
                .where(UserModel.user_id == user_id)
            )
            telegram_id = await self.session.execute(stmt)
            return telegram_id.scalar()
        except SQLAlchemyError as ex:
            await self.session.rollback()
            raise RuntimeError(f"Error while reading telegram_id: {ex}")

    async def get_telegram_id_by_phone_number(self, phone_number: str) -> int:
        try:
            stmt = (
                select(UserModel.telegram_id)
                .where(UserModel.phone_number == phone_number)
            )
            telegram_id = await self.session.execute(stmt)
            return telegram_id.scalar_one_or_none()
        except SQLAlchemyError as ex:
            await self.session.rollback()
            raise RuntimeError(f"Error while reading telegram id by phone_number: {ex}")

    async def get_phone_number_by_telegram_id(self, telegram_id: int) -> Optional[str]:
        try:
            stmt = (
                select(UserModel.phone_number)
                .where(UserModel.telegram_id == telegram_id)
            )
            phone_number = await self.session.execute(stmt)
            return phone_number.scalar()
        except SQLAlchemyError as ex:
            await self.session.rollback()
            raise RuntimeError(f"Error while reading phone_number: {ex}")

    async def get_telegram_ids(self) -> Sequence[int]:
        try:
            stmt = (select(UserModel.telegram_id))
            telegram_id = await self.session.execute(stmt)
            return telegram_id.scalar()
        except SQLAlchemyError as ex:
            await self.session.rollback()
            raise RuntimeError(f"Error while reading telegram_id: {ex}")

    async def get_telegram_ids_by_phone_numbers(self, phone_numbers: List[str]) -> Sequence[int]:
        try:
            telegram_ids: List[int] = []
            for phone_number in phone_numbers:
                stmt = (
                    select(UserModel.telegram_id)
                    .where(UserModel.phone_number == phone_number)
                )
                telegram_id = await self.session.execute(stmt)
                telegram_ids.append(telegram_id.scalar())
            return telegram_ids
        except SQLAlchemyError as ex:
            await self.session.rollback()
            raise RuntimeError(f"Error while reading telegram_id: {ex}")

    async def get_telegram_ids_by_user_ids(self, user_ids: List[str]) -> Sequence[int]:
        try:
            telegram_ids: List[int] = []
            for user_id in user_ids:
                stmt = (
                    select(UserModel.telegram_id)
                    .where(UserModel.user_id == user_id)
                )
                telegram_id = await self.session.execute(stmt)
                telegram_ids.append(telegram_id.scalar())
            return telegram_ids
        except SQLAlchemyError as ex:
            await self.session.rollback()
            raise RuntimeError(f"Error while reading telegram_id: {ex}")

    async def count(self) -> int:
        try:
            stmt = (
                select(func.count())
                .select_from(UserModel)
            )
            count = await self.session.execute(stmt)
            return count.scalar()
        except SQLAlchemyError as ex:
            await self.session.rollback()
            raise RuntimeError(f"Error while reading users count: {ex}")

    async def count_phone_numbers(self) -> int:
        try:
            stmt = (
                select(func.count())
                .select_from(UserModel.phone_number)
            )
            count = await self.session.execute(stmt)
            return count.scalar()
        except SQLAlchemyError as ex:
            await self.session.rollback()
            raise RuntimeError(f"Error while reading users count: {ex}")

    async def count_registered(self) -> int:
        try:
            stmt = (
                select(func.count())
                .select_from(UserModel.user_id)
            )
            count = await self.session.execute(stmt)
            return count.scalar()
        except SQLAlchemyError as ex:
            await self.session.rollback()
            raise RuntimeError(f"Error while reading users count: {ex}")

    async def count_daily(self) -> Sequence[Tuple[datetime, int]]:
        try:
            stmt = (
                select(
                    func.date(UserModel.created_at).label("date"),
                    func.count().label("count")
                )
                .group_by(func.date(UserModel.created_at))
                .order_by(func.date(UserModel.created_at))
            )
            count = await self.session.execute(stmt)
            return list(count.scalars().all())
        except SQLAlchemyError as ex:
            await self.session.rollback()
            raise RuntimeError(f"Error while reading users daily count: {ex}")
