from dishka import Provider, provide, Scope

from src.repository import DialogRepository
from src.core.use_cases import ChatsUseCase


class ChatsProvider(Provider):
    @provide(scope=Scope.APP)
    def get_chats_use_case(self, dialog_repository: DialogRepository) -> ChatsUseCase:
        return ChatsUseCase(dialog_repository)
