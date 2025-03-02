from dishka import Provider, Scope, provide

from src.repository import UserRepository
from src.core.use_cases import UserUseCase


class UserProvider(Provider):
    @provide(scope=Scope.APP)
    def get_user_use_case(
        self, 
        user_repository: UserRepository
    ) -> UserUseCase:
        return UserUseCase(user_repository)
