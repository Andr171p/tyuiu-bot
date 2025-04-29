from typing import Optional

from ..entities import User, Contact, SharingContactStatus
from ..interfaces import UserRepository, ContactRepository, UserRegistration


class UserService:
    def __init__(
            self,
            user_repository: UserRepository,
            contact_repository: ContactRepository,
            user_registration: UserRegistration
    ) -> None:
        self._user_repository = user_repository
        self._contact_repository = contact_repository
        self._user_registration = user_registration

    async def save(self, telegram_id: int, username: Optional[str]) -> None:
        if await self._user_repository.read(telegram_id):
            return
        user = User(telegram_id=telegram_id, username=username)
        await self._user_repository.create(user)

    async def share_contact(self, telegram_id: int, phone_number: str) -> SharingContactStatus:
        created_contact = await self._contact_repository.read(telegram_id)
        status = SharingContactStatus.SUCCESS
        if created_contact.is_registered:
            return SharingContactStatus.ALREADY_SHARED
        elif not created_contact.is_registered:
            return SharingContactStatus.NOT_REGISTERED
        user_id = await self._user_registration.get_user_id(phone_number)
        is_registered = True if user_id else False
        if not is_registered:
            status = SharingContactStatus.NOT_REGISTERED
        contact = Contact(
            telegram_id=telegram_id,
            phone_number=phone_number,
            is_registered=is_registered
        )
        created_contact = await self._contact_repository.create(contact)
        if not created_contact:
            return SharingContactStatus.ERROR
        await self._user_repository.update(telegram_id, user_id)
        return status
