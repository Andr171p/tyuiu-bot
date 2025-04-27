from datetime import datetime

from typing import List, Tuple, Optional

from sqlalchemy import select, update, func
from sqlalchemy.ext.asyncio import AsyncSession

from src.core.entities import Contact
from src.core.interfaces import ContactRepository
from src.infrastructure.database.models import ContactModel


class SQLContactRepository(ContactRepository):
    def __init__(self, session: AsyncSession) -> None:
        self._session = session

    async def create(self, contact: Contact) -> int:
        self._session.add(ContactModel(**contact.model_dump()))
        await self._session.flush()
        id = contact.id
        await self._session.commit()
        return id

    async def read(self, user_id: int) -> Optional[Contact]:
        stmt = (
            select(ContactModel)
            .where(ContactModel.user_id == user_id)
        )
        result = await self._session.execute(stmt)
        contact = result.scalar_one_or_none()
        return Contact.model_validate(contact) if contact is not None else None

    async def read_by_phone_number(self, phone_number: str) -> Optional[Contact]:
        stmt = (
            select(ContactModel)
            .where(ContactModel.phone_number == phone_number)
        )
        result = await self._session.execute(stmt)
        contact = result.scalar_one_or_none()
        return Contact.model_validate(contact) if contact is not None else None

    async def read_user_id_by_phone_number(self, phone_number: str) -> int:
        stmt = (
            select(ContactModel.user_id)
            .where(ContactModel.phone_number == phone_number)
        )
        user_id = await self._session.execute(stmt)
        return user_id.scalar()

    async def read_phone_number_by_user_id(self, user_id: int) -> str:
        stmt = (
            select(ContactModel.phone_number)
            .where(ContactModel.user_id == user_id)
        )
        phone_number = await self._session.execute(stmt)
        return phone_number.scalar()

    async def read_is_exists(self, is_exists: bool = True) -> List[Optional[Contact]]:
        stmt = (
            select(ContactModel)
            .where(ContactModel.is_exists == is_exists)
        )
        results = await self._session.execute(stmt)
        contacts = results.scalars().all()
        return [Contact.model_validate(contact) for contact in contacts] if contacts else []

    async def list(self) -> List[Contact]:
        stmt = select(ContactModel)
        results = await self._session.execute(stmt)
        contacts = results.scalars().all()
        return [Contact.model_validate(contact) for contact in contacts]

    async def list_user_ids(self) -> List[int]:
        stmt = select(ContactModel.user_id)
        user_ids = await self._session.execute(stmt)
        return list(user_ids.scalars().all())

    async def paginate(self, page: int, limit: int) -> List[Optional[Contact]]:
        offset = (page - 1) * limit
        stmt = (
            select(ContactModel)
            .offset(offset)
            .limit(limit)
        )
        results = await self._session.execute(stmt)
        contacts = results.scalars().all()
        return [Contact.model_validate(contact) for contact in contacts] if contacts else []

    async def update(self, user_id: int, is_exists: bool) -> Optional[Contact]:
        stmt = (
            update(ContactModel)
            .where(ContactModel.user_id == user_id)
            .values(is_exists=is_exists)
        )
        result = await self._session.execute(stmt)
        await self._session.commit()
        contact = result.scalar_one_or_none()
        return Contact.model_validate(contact) if contact is not None else None

    async def count(self) -> int:
        stmt = (
            select(func.count())
            .select_from(ContactModel)
        )
        count = await self._session.execute(stmt)
        return count.scalar()

    async def count_daily(self) -> List[Tuple[datetime, int]]:
        stmt = (
            select(
                func.date(ContactModel.created_at).label("date"),
                func.count().label("count")
            )
            .group_by(func.date(ContactModel.created_at))
            .order_by(func.date(ContactModel.created_at))
        )
        count = await self._session.execute(stmt)
        return list(count.scalars().all())
