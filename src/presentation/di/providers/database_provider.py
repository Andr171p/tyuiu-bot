from dishka import Provider, provide, Scope

from src.database.database_manager import DatabaseManager
from src.database.crud import UserCRUD, ContactCRUD, DialogCRUD
from src.config import settings


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
