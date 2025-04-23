from dishka import Provider, provide, Scope

from src.infrastructure.database.session import DatabaseManager
from src.infrastructure.database.crud import UserCRUD, ContactCRUD, DialogCRUD
from src.settings import settings


class DatabaseProvider(Provider):
    @provide(scope=Scope.APP)
    def get_database_manager(self) -> DatabaseManager:
        return DatabaseManager(settings.db.url)

    @provide(scope=Scope.APP)
    def get_user_crud(self, manager: DatabaseManager) -> UserCRUD:
        return UserCRUD(manager)

    @provide(scope=Scope.APP)
    def get_contact_crud(self, manager: DatabaseManager) -> ContactCRUD:
        return ContactCRUD(manager)

    @provide(scope=Scope.APP)
    def get_dialog_crud(self, manager: DatabaseManager) -> DialogCRUD:
        return DialogCRUD(manager)
