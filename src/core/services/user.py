from typing import Optional

from ..entities import User, UserShareContact, SharingContactStatus
from ..interfaces import UserRepository, UserRegistration


class UserService:
    def __init__(
            self,
            user_repository: UserRepository,
            user_registration: UserRegistration
    ) -> None:
        self._user_repository = user_repository
        self._user_registration = user_registration

    async def save(self, telegram_id: int, username: Optional[str]) -> None:
        if await self._user_repository.read(telegram_id):
            return
        user = User(telegram_id=telegram_id, username=username)
        await self._user_repository.create(user)

    async def share_contact(self, telegram_id: int, phone_number: str) -> SharingContactStatus:
        user = await self._user_repository.read(telegram_id)
        status = SharingContactStatus.SUCCESS
        if user.user_id and user.phone_number:
            return SharingContactStatus.ALREADY_SHARED
        elif not user.user_id and user.phone_number:
            return SharingContactStatus.NOT_REGISTERED
        user_id = await self._user_registration.get_user_id(phone_number)
        is_registered = True if user_id else False
        if not is_registered:
            status = SharingContactStatus.NOT_REGISTERED
        updated_user = await self._user_repository.update(
            telegram_id,
            user_id=user_id,
            phone_number=phone_number
        )
        if not updated_user:
            return SharingContactStatus.ERROR
        return status
