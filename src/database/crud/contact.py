from typing import Sequence

from sqlalchemy import select

from src.database.models import Contact
from src.database.context import DBContext


class ContactCRUD(DBContext):
    def __init__(self) -> None:
        super().__init__()
        self.init()

    async def read_by_user_id(self, user_id: int) -> Contact | None:
        async with self.session() as session:
            stmt = (
                select(Contact)
                .where(Contact.user_id == user_id)
            )
            contact = await session.execute(stmt)
        return contact.scalar_one_or_none()

    async def read_by_phone_number(self, phone_number: str) -> Contact | None:
        async with self.session() as session:
            stmt = (
                select(Contact)
                .where(Contact.phone_number == phone_number)
            )
            contact = await session.execute(stmt)
        return contact.scalar_one_or_none()

    async def read_all(self) -> Sequence[Contact]:
        async with self.session() as session:
            stmt = select(Contact)
            contacts = await session.execute(stmt)
        return contacts.scalars().all()

    async def create(self, contact: Contact) -> Contact:
        async with self.session() as session:
            session.add(contact)
            await session.commit()
        return contact
