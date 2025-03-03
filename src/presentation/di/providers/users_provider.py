from dishka import Provider, provide, Scope

from src.repository import UserRepository
from src.repository import ContactRepository
from src.core.use_cases import UsersUseCase


class UsersProvider(Provider):
    @provide(scope=Scope.APP)
    def get_users_use_case(
            self,
            users_repository: UserRepository,
            contact_repository: ContactRepository
    ) -> UsersUseCase:
        return UsersUseCase(users_repository, contact_repository)
