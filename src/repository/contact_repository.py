from typing import TYPE_CHECKING, List, Union, Sequence

if TYPE_CHECKING:
    from src.database.crud import ContactCRUD

from src.repository.base_repository import BaseRepository
from src.database.models import ContactModel
from src.core.entities import Contact
from src.dto import PerDayDistribution


class ContactRepository(BaseRepository):
    def __init__(self, crud: "ContactCRUD") -> None:
        self._crud = crud
        
    async def save(self, contact: Contact) -> int:
        id = await self._crud.create(ContactModel(**contact.model_dump()))
        return id
    
    async def get_by_user_id(self, user_id: int) -> Union[Contact, None]:
        contact = await self._crud.read_by_user_id(user_id)
        return Contact.model_validate(contact) if contact else None
    
    async def get_all(self) -> List[Union[Contact, None]]:
        contacts = await self._crud.read_all()
        return [Contact.model_validate(contact) for contact in contacts] if contacts else []

    async def get_user_id_by_phone_number(self, phone_number: str) -> Union[int, None]:
        return await self._crud.read_user_id_by_phone_number(phone_number)

    async def get_phone_number_by_user_id(self, user_id: int) -> Union[str, None]:
        return await self._crud.read_phone_number_by_user_id(user_id)

    async def get_all_user_ids(self) -> Sequence[Union[int, None]]:
        user_ids = await self._crud.read_all_user_ids()
        return user_ids if user_ids else []
    
    async def get_total_count(self) -> int:
        count = await self._crud.read_total_count()
        return count if count else 0

    async def get_count_per_day(self) -> List[PerDayDistribution]:
        per_days_counts = await self._crud.read_count_per_day()
        return [PerDayDistribution(date=date, count=count) for date, count in per_days_counts]
