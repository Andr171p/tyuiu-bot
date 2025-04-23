from datetime import datetime

from typing import Any, Sequence, Tuple, Optional
    
from sqlalchemy import select, update, func
from sqlalchemy.ext.asyncio import AsyncSession

from src.infrastructure.database.models import ContactModel
from src.infrastructure.database.crud.abstract_crud import AbstractCRUD


class ContactCRUD(AbstractCRUD):
    def __init__(self, session: AsyncSession) -> None:
        self._session = session
    
    async def create(self, contact: ContactModel) -> int:
        self._session.add(contact)
        await self._session.flush()
        id = contact.id
        await self._session.commit()
        return id
    
    async def read(self, user_id: int) -> Optional[ContactModel]:
        stmt = (
            select(ContactModel)
            .where(ContactModel.user_id == user_id)
        )
        contact = await self._session.execute(stmt)
        return contact.scalar_one_or_none()
    
    async def read_by_phone_number(self, phone_number: str) -> Optional[ContactModel]:
        stmt = (
            select(ContactModel)
            .where(ContactModel.phone_number == phone_number)
        )
        contact = await self._session.execute(stmt)
        return contact.scalar_one_or_none()
    
    async def read_all(self) -> Sequence[ContactModel]:
        stmt = select(ContactModel)
        contacts = await self._session.execute(stmt)
        return contacts.scalars().all()

    async def read_user_id_by_phone_number(self, phone_number: str) -> Optional[int]:
        stmt = (
            select(ContactModel.user_id)
            .where(ContactModel.phone_number == phone_number)
        )
        user_id = await self._session.execute(stmt)
        return user_id.scalar_one_or_none()

    async def read_phone_number_by_user_id(self, user_id: int) -> Optional[str]:
        stmt = (
            select(ContactModel.phone_number)
            .where(ContactModel.user_id == user_id)
        )
        phone_number = await self._session.execute(stmt)
        return phone_number.scalar_one_or_none()

    async def read_all_user_ids(self) -> Sequence[int]:
        stmt = select(ContactModel.user_id)
        user_ids = await self._session.execute(stmt)
        return user_ids.scalars().all()
    
    async def read_total_count(self) -> int:
        stmt = (
            select(func.count())
            .select_from(ContactModel)
        )
        total_count = await self._session.execute(stmt)
        return total_count.scalar_one_or_none()

    async def read_date_to_count(self) -> Sequence[Tuple[datetime, int]]:
        stmt = (
            select(
                func.date(ContactModel.created_at).label("date"),
                func.count().label("count")
            )
            .group_by(func.date(ContactModel.created_at))
            .order_by(func.date(ContactModel.created_at))
        )
        date_to_count = await self._session.execute(stmt)
        return date_to_count.scalars().all()

    async def read_exists(self, is_exists: bool = True) -> Sequence[ContactModel]:
        stmt = (
            select(ContactModel)
            .where(ContactModel.is_exists == is_exists)
        )
        contacts = await self._session.execute(stmt)
        return contacts.scalars().all()

    async def update(self, user_id: int, **kwargs: Any) -> ContactModel:
        stmt = (
            update(ContactModel)
            .where(ContactModel.user_id == user_id)
            .values(**kwargs)
        )
        contact = await self._session.execute(stmt)
        return contact.scalar_one_or_none()
