from dishka import Provider, provide, Scope

from src.database.crud import UserCRUD, ChatCRUD, ContactCRUD
from src.repository import UserRepository, ContactRepository, ChatRepository


class RepositoryProvider(Provider):
    @provide(scope=Scope.APP)
    def get_user_repository(self, crud: UserCRUD) -> UserRepository:
        return UserRepository(crud)

    @provide(scope=Scope.APP)
    def get_contact_repository(self, crud: ContactCRUD) -> ContactRepository:
        return ContactRepository(crud)

    @provide(scope=Scope.APP)
    def get_chat_repository(self, crud: ChatCRUD) -> ChatRepository:
        return ChatRepository(crud)
