from src.core.entities import User, Contact, ChatHistory, ChatHistoryPage
from src.repository import UserRepository, ContactRepository, DialogRepository


class UsersUseCase:
    def __init__(
        self, 
        user_repository: UserRepository,
        contact_repository: ContactRepository,
        dialog_repository: DialogRepository
    ) -> None:
        self._user_repository = user_repository
        self._contact_repository = contact_repository
        self._dialog_repository = dialog_repository
        
    async def register(self, user: User) -> None:
        if await self._user_repository.get_by_user_id(user.user_id):
            return
        await self._user_repository.save(user)
        
    async def share_contact(self, contact: Contact) -> None:
        await self._contact_repository.save(contact)

    async def get_chat_history(self, user_id: int) -> ChatHistory:
        dialogs = await self._dialog_repository.get_by_user_id(user_id)
        return ChatHistory(
            user_id=user_id,
            dialogs=dialogs
        )

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
