from dishka import Provider, Scope, provide

from src.apis import ChatBotAPI
from src.repository import ChatRepository
from src.core.use_cases import ChatBotUseCase


class ChatBotProvider(Provider):
    @provide(scope=Scope.APP)
    def get_chat_bot_api(self, base_url: str) -> ChatBotAPI:
        return ChatBotAPI(base_url)
    
    @provide(scope=Scope.APP)
    def get_chat_bot_use_case(
        self,
        chat_bot_api: ChatBotAPI,
        chat_repository: ChatRepository,
    ) -> ChatBotUseCase:
        return ChatBotUseCase(
            chat_bot_api=chat_bot_api,
            chat_repository=chat_repository
        )
