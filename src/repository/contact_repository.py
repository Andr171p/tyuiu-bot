from typing import List, Optional, Union, Sequence

from src.infrastructure.database.models import ContactModel
from src.infrastructure.database.crud import ContactCRUD
from src.core.interfaces import AbstractRepository
from src.core.entities import Contact


class ContactRepository(AbstractRepository):
    def __init__(self, crud: ContactCRUD) -> None:
        self._crud = crud
        
    async def save(self, contact: Contact) -> int:
        return await self._crud.create(ContactModel(**contact.model_dump()))
    
    async def get(self, user_id: int) -> Optional[Contact]:
        contact = await self._crud.read_by_user_id(user_id)
        return Contact.model_validate(contact) if contact else None
    
    async def list(self) -> List[Optional[Contact]]:
        contacts = await self._crud.read_all()
        return [Contact.model_validate(contact) for contact in contacts] if contacts else []

    async def get_user_id_by_phone_number(self, phone_number: str) -> Optional[int]:
        return await self._crud.read_user_id_by_phone_number(phone_number)

    async def get_phone_number_by_user_id(self, user_id: int) -> Optional[str]:
        return await self._crud.read_phone_number_by_user_id(user_id)

    async def list_user_ids(self) -> Sequence[Optional[int]]:
        user_ids = await self._crud.read_all_user_ids()
        return user_ids if user_ids else []
    
    async def total_count(self) -> int:
        return await self._crud.read_total_count()
