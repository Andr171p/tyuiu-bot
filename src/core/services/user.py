from ..interfaces import UserRepository, UserRegistration
from ..entities import User, ShareContactUser, SharingContactStatus


class UserService:
    def __init__(
            self,
            user_repository: UserRepository,
            user_registration: UserRegistration
    ) -> None:
        self._user_repository = user_repository
        self._user_registration = user_registration

    async def save(self, user: ShareContactUser) -> SharingContactStatus:
        created_user = await self._user_repository.read(user.telegram_id)
        status = SharingContactStatus.SUCCESS
        if created_user.user_id and created_user.phone_number:
            return SharingContactStatus.ALREADY_SHARED
        elif not created_user.user_id and created_user.phone_number:
            return SharingContactStatus.NOT_REGISTERED
        user_id = await self._user_registration.get_user_id(user.phone_number)
        is_registered = True if user_id else False
        if not is_registered:
            status = SharingContactStatus.NOT_REGISTERED
        await self._user_repository.create(User(
            telegram_id=user.telegram_id,
            first_name=user.first_name,
            last_name=user.last_name,
            username=user.username,
            user_id=user_id,
            phone_number=user.phone_number
        ))
        return status
