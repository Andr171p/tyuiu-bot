from typing import TYPE_CHECKING, Sequence

if TYPE_CHECKING:
    from src.db.database_manager import DatabaseManager
    
from sqlalchemy import select, func

from src.db.crud.base_crud import BaseCRUD
from src.db.models import ContactModel


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
    
    async def read_total_count(self) -> int | None:
        async with self._manager.session() as session:
            stmt = (
                select(func.count)
                .select_from(ContactModel)
            )
            contacts_count = await session.execute(stmt)
        return contacts_count.scalar_one_or_none()
