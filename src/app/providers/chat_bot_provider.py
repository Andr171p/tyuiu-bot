from dishka import Provider, Scope, provide

from src.apis import ChatBotAPI
from src.repository import DialogRepository
from src.core.use_cases import ChatBotUseCase


class ChatBotProvider(Provider):
    @provide(scope=Scope.APP)
    def get_chat_bot(
        self,
        chat_bot_api: ChatBotAPI,
        dialog_repository: DialogRepository,
    ) -> ChatBotUseCase:
        return ChatBotUseCase(
            chat_bot_api=chat_bot_api,
            dialog_repository=dialog_repository
        )
