from dishka import Provider, provide, Scope

from src.repository import UserRepository, ContactRepository, DialogRepository
from src.core.use_cases import UsersUseCase
from src.controllers import UsersController
from src.infrastructure.apis import AuthAPI
from src.config import settings


class UsersProvider(Provider):
    @provide(scope=Scope.APP)
    def get_auth_api(self) -> AuthAPI:
        return AuthAPI(settings.auth.base_url)

    @provide(scope=Scope.APP)
    def get_users_use_case(
            self,
            user_repository: UserRepository,
            contact_repository: ContactRepository,
            dialog_repository: DialogRepository,
            auth_api: AuthAPI
    ) -> UsersUseCase:
        return UsersUseCase(
            user_repository=user_repository,
            contact_repository=contact_repository,
            dialog_repository=dialog_repository,
            auth_api=auth_api
        )

    @provide(scope=Scope.APP)
    def get_users_controller(self, users_use_case: UsersUseCase) -> UsersController:
        return UsersController(users_use_case)
