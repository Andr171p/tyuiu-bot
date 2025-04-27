from src.core.entities import User, Contact
from src.core.interfaces import UserRepository, ContactRepository, UserRegistration


class UserManager:
    def __init__(
            self,
            user_repository: UserRepository,
            contact_repository: ContactRepository,
            user_registration: UserRegistration
    ) -> None:
        self._user_repository = user_repository
        self._contact_repository = contact_repository
        self._user_registration = user_registration

    async def register(self, user: User) -> bool:
        if await self._user_repository.get(user.user_id):
            return False
        id = self._user_repository.save(user)
        return True if id else False

    async def share_contact(self, contact: Contact) -> bool:
        if await self._contact_repository.get(contact.user_id):
            return False
        id = self._contact_repository.save(contact)
        return True if id else False

    async def is_exists(self, user_id: int) -> bool:
        phone_number = await self._contact_repository.get_phone_number_by_user_id(user_id)
        return await self._user_auth_gateway.check_exists(phone_number)

    async def change_exists_status(self, user_id: int, is_exists: bool) -> bool:
        contact = await self._contact_repository.update(user_id, is_exists=is_exists)
        return True if contact else False
