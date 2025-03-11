from dishka import Provider, provide, Scope

from src.core.use_cases import UsersUseCase
from src.controllers import ChatsController


class ChatsProvider(Provider):
    @provide(scope=Scope.APP)
    def get_chats_controller(self, users_use_case: UsersUseCase) -> ChatsController:
        return ChatsController(users_use_case)
