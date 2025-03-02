from src.core.entities import User, Contact
from src.repository import UserRepository, ContactRepository


class UsersUseCase:
    def __init__(
        self, 
        user_repository: UserRepository,
        contact_repository: ContactRepository
    ) -> None:
        self._user_repository = user_repository
        self._contact_repository = contact_repository
        
    async def register(self, user: User) -> None:
        if await self._user_repository.get_by_user_id(user.user_id):
            return
        await self._user_repository.save(user)
        
    async def share_contact(self, contact: Contact) -> None:
        await self._contact_repository.save(contact)
    
    async def get_users_count(self) -> int:
        return await self._user_repository.get_total_count()
