from typing import TYPE_CHECKING, List, Union

if TYPE_CHECKING:
    from src.database.crud import ContactCRUD

from src.repository.base_repository import BaseRepository
from src.database.models import ContactModel
from src.core.entities import Contact


class ContactRepository(BaseRepository):
    def __init__(self, crud: "ContactCRUD") -> None:
        self._crud = crud
        
    async def add(self, contact: Contact) -> int:
        id = await self._crud.create(ContactModel(**contact.model_dump()))
        return id
    
    async def get_by_user_id(self, user_id: int) -> Union[Contact, None]:
        contact = await self._crud.read_by_user_id(user_id)
        return Contact.model_validate(contact) if contact else None
    
    async def get_all(self) -> List[Union[Contact, None]]:
        contacts = await self._crud.read_all()
        return [Contact.model_validate(contact) for contact in contacts] if contacts else []
    
    async def get_total_count(self) -> int:
        count = await self._crud.read_total_count()
        return count if count else 0
