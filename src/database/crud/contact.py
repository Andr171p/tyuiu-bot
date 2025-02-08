from typing import Sequence

from sqlalchemy import select

from src.database.models import Contact
from src.database.interfaces import BaseCRUD
from src.database.manager_provider import get_database_manager


class ContactCRUD(BaseCRUD):
    def __init__(self, manager = get_database_manager()) -> None:
        self._manager = manager
        
    async def create(self, contact: Contact) -> Contact:
        async with self._manager.session() as session:
            session.add(contact)
            await session.commit()
        return contact

    async def read_by_user_id(self, user_id: int) -> Contact | None:
        async with self._manager.session() as session:
            stmt = (
                select(Contact)
                .where(Contact.user_id == user_id)
            )
            contact = await session.execute(stmt)
        return contact.scalar_one_or_none()

    async def read_by_phone_number(self, phone_number: str) -> Contact | None:
        async with self._manager.session() as session:
            stmt = (
                select(Contact)
                .where(Contact.phone_number == phone_number)
            )
            contact = await session.execute(stmt)
        return contact.scalar_one_or_none()

    async def read_all(self) -> Sequence[Contact]:
        async with self._manager.session() as session:
            stmt = select(Contact)
            contacts = await session.execute(stmt)
        return contacts.scalars().all()
