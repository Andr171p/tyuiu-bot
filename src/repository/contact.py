from typing import List

from src.repository.base import BaseRepository
from src.database.crud import ContactCRUD
from src.database.models import Contact
from src.schemas import ContactSchema


class ContactRepository(BaseRepository):
    crud = ContactCRUD()

    async def add(self, contact: ContactSchema) -> ContactSchema:
        added_contact = await self.crud.create(Contact(**contact.model_dump()))
        return ContactSchema(**added_contact.__dict__)

    async def get_by_user_id(self, user_id: int) -> ContactSchema | None:
        contact = await self.crud.read_by_user_id(user_id)
        if contact is None:
            return
        return ContactSchema(**contact.__dict__)

    async def get_by_phone_number(self, phone_number: str) -> ContactSchema | None:
        contact = await self.crud.read_by_phone_number(phone_number)
        if contact is None:
            return
        return ContactSchema(**contact.__dict__)

    async def get_all(self) -> List[ContactSchema] | None:
        contacts = await self.crud.read_all()
        return [ContactSchema(**contact.__dict__) for contact in contacts]
