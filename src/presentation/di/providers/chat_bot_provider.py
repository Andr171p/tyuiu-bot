from dishka import Provider, provide, Scope

from src.apis import ChatBotAPI
from src.core.use_cases import ChatBotUseCase
from src.config import settings


class ChatBotProvider(Provider):
    @provide(scope=Scope.APP)
    def get_chat_bot_api(
            self,
            base_url: str = settings.chat_bot_api.base_url
    ) -> ChatBotAPI:
        return ChatBotAPI(base_url)

    @provide(scope=Scope.APP)
    def get_chat_bot_use_case(self, chat_bot_api: ChatBotAPI) -> ChatBotUseCase:
        return ChatBotUseCase(chat_bot_api)