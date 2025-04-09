from src.core.entities import User, Contact, ChatHistory, ChatHistoryPage
from src.repository import UserRepository, ContactRepository, DialogRepository
from src.apis import AuthAPI


class UsersUseCase:
    def __init__(
        self, 
        user_repository: UserRepository,
        contact_repository: ContactRepository,
        dialog_repository: DialogRepository,
        auth_api: AuthAPI
    ) -> None:
        self._user_repository = user_repository
        self._contact_repository = contact_repository
        self._dialog_repository = dialog_repository
        self._auth_api = auth_api
        
    async def register(self, user: User) -> None:
        if await self._user_repository.get_by_user_id(user.user_id):
            return
        await self._user_repository.save(user)
        
    async def share_contact(self, contact: Contact) -> None:
        if await self._contact_repository.get_by_user_id(contact.user_id):
            return
        await self._contact_repository.save(contact)

    async def get_chat_history(self, user_id: int) -> ChatHistory:
        dialogs = await self._dialog_repository.get_by_user_id(user_id)
        return ChatHistory(
            user_id=user_id,
            dialogs=dialogs
        )

    async def check_exist(self, user_id: int) -> bool:
        contact = await self._contact_repository.get_by_user_id(user_id)
        return await self._auth_api.check_user_exists_by_phone_number(contact.phone_number)

    async def get_page_of_chat_history(
            self,
            user_id: int,
            page: int,
            limit: int = 5
    ) -> ChatHistoryPage:
        dialogs = await self._dialog_repository.get_by_user_id_with_limit(
            user_id=user_id,
            page=page,
            limit=limit
        )
        total = await self._dialog_repository.get_total_count()
        return ChatHistoryPage(
            user_id=user_id,
            total=total,
            page=page,
            limit=limit,
            dialogs=dialogs
        )
