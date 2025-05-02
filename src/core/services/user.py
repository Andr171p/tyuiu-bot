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

    async def share_contact(self, user_contact: ShareContactUser) -> SharingContactStatus:
        existing_user = await self._user_repository.read(user_contact.telegram_id)
        if existing_user:
            return self.__handle_existing_user(existing_user)
        return await self.__save_new_user(user_contact)

    @staticmethod
    def __handle_existing_user(user: User) -> SharingContactStatus:
        if user.user_id and user.phone_number:
            return SharingContactStatus.ALREADY_SHARED
        if user.phone_number:
            return SharingContactStatus.NOT_REGISTERED
        return SharingContactStatus.SUCCESS

    async def __save_new_user(self, user_contact: ShareContactUser) -> SharingContactStatus:
        user_id = await self._user_registration.get_user_id(user_contact.phone_number)
        status = SharingContactStatus.NOT_REGISTERED if not user_id else SharingContactStatus.SUCCESS
        new_user = User(
            telegram_id=user_contact.telegram_id,
            first_name=user_contact.first_name,
            last_name=user_contact.last_name,
            username=user_contact.username,
            user_id=user_id,
            phone_number=user_contact.phone_number
        )
        await self._user_repository.create(new_user)
        return status
