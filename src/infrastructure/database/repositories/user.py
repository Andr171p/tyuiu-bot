from typing import Optional

from sqlalchemy import select, update
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.ext.asyncio import AsyncSession

from src.constants import USER_STATUSES
from src.core.dto import UserReadDTO
from src.core.entities import User
from src.core.interfaces import UserRepository
from ..models import UserModel


class SQLUserRepository(UserRepository):
    def __init__(self, session: AsyncSession) -> None:
        self.session = session

    async def create(self, user: User) -> None:
        try:
            user_model = UserModel(**user.model_dump())
            self.session.add(user_model)
            await self.session.commit()
        except SQLAlchemyError as e:
            await self.session.rollback()
            raise RuntimeError(f"Error while creating user: {e}")

    async def read(self, telegram_id: int) -> Optional[UserReadDTO]:
        try:
            stmt = (
                select(UserModel)
                .where(UserModel.telegram_id == telegram_id)
            )
            result = await self.session.execute(stmt)
            user = result.scalar_one_or_none()
            return UserReadDTO.model_validate(user) if user else None
        except SQLAlchemyError as e:
            await self.session.rollback()
            raise RuntimeError(f"Error while reading user: {e}")

    async def update(self, phone_number: str, **kwargs) -> Optional[UserReadDTO]:
        try:
            stmt = (
                update(UserModel)
                .where(UserModel.phone_number == phone_number)
                .values(**kwargs)
                .returning(UserModel)
            )
            result = await self.session.execute(stmt)
            user = result.scalar_one_or_none()
            await self.session.commit()
            return UserReadDTO.model_validate(user) if user else None
        except SQLAlchemyError as ex:
            await self.session.rollback()
            raise RuntimeError(f"Error while updating user: {ex}")

    async def get_by_status(self, status: USER_STATUSES = "READY") -> list[UserReadDTO]:
        try:
            stmt = (
                select(UserModel)
                .where(UserModel.status == status)
            )
            results = await self.session.execute(stmt)
            users = results.scalars().all()
            return [UserReadDTO.model_validate(user) for user in users]
        except SQLAlchemyError as e:
            await self.session.rollback()
            raise RuntimeError(f"Error while reading by status: {e}")

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
            raise RuntimeError(f"Error while reading by user id: {ex}")
