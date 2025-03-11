from typing import TYPE_CHECKING, Sequence, List, Tuple
from datetime import datetime

if TYPE_CHECKING:
    from src.database.database_manager import DatabaseManager
    
from sqlalchemy import select, func

from src.database.crud.base_crud import BaseCRUD
from src.database.models import ContactModel


class ContactCRUD(BaseCRUD):
    def __init__(self, manager: "DatabaseManager") -> None:
        self._manager = manager
    
    async def create(self, contact: ContactModel) -> int:
        async with self._manager.session() as session:
            session.add(contact)
            id = contact.id
            await session.commit()
        return id
    
    async def read_by_user_id(self, user_id: int) -> ContactModel | None:
        async with self._manager.session() as session:
            stmt = (
                select(ContactModel)
                .where(ContactModel.user_id == user_id)
            )
            contact = await session.execute(stmt)
        return contact.scalar_one_or_none()
    
    async def read_by_phone_number(self, phone_number: str) -> ContactModel | None:
        async with self._manager.session() as session:
            stmt = (
                select(ContactModel)
                .where(ContactModel.phone_number == phone_number)
            )
            contact = await session.execute(stmt)
        return contact.scalar_one_or_none()
    
    async def read_all(self) -> Sequence[ContactModel] | None:
        async with self._manager.session() as session:
            stmt = select(ContactModel)
            contacts = await session.execute(stmt)
        return contacts.scalars().all()

    async def read_user_id_by_phone_number(self, phone_number: str) -> int | None:
        async with self._manager.session() as session:
            stmt = (
                select(ContactModel.user_id)
                .where(ContactModel.phone_number == phone_number)
            )
            user_id = await session.execute(stmt)
        return user_id.scalar_one_or_none()

    async def read_phone_number_by_user_id(self, user_id: int) -> str | None:
        async with self._manager.session() as session:
            stmt = (
                select(ContactModel.phone_number)
                .where(ContactModel.user_id == user_id)
            )
            phone_number = await session.execute(stmt)
        return phone_number.scalar_one_or_none()

    async def read_all_user_ids(self) -> Sequence[int] | None:
        async with self._manager.session() as session:
            stmt = select(ContactModel.user_id)
            user_ids = await session.execute(stmt)
        return user_ids.scalars().all()
    
    async def read_total_count(self) -> int | None:
        async with self._manager.session() as session:
            stmt = (
                select(func.count())
                .select_from(ContactModel)
            )
            contacts_count = await session.execute(stmt)
        return contacts_count.scalar_one_or_none()

    async def read_count_per_day(self) -> List[Tuple[datetime, int]]:
        async with self._manager.session() as session:
            stmt = (
                select(
                    func.date(ContactModel.created_at).label("date"),
                    func.count().label("count")
                )
                .group_by(func.date(ContactModel.created_at))
                .order_by(func.date(ContactModel.created_at))
            )
            counts_per_days = await session.execute(stmt)
        return counts_per_days.all()
