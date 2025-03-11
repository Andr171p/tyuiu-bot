from dishka import Provider, provide, Scope

from src.repository import UserRepository, ContactRepository, DialogRepository
from src.core.use_cases import UsersUseCase
from src.controllers import UsersController


class UsersProvider(Provider):
    @provide(scope=Scope.APP)
    def get_users_use_case(
            self,
            users_repository: UserRepository,
            contact_repository: ContactRepository,
            dialog_repository: DialogRepository
    ) -> UsersUseCase:
        return UsersUseCase(users_repository, contact_repository, dialog_repository)

    @provide(scope=Scope.APP)
    def get_users_controller(self, users_use_case: UsersUseCase) -> UsersController:
        return UsersController(users_use_case)
