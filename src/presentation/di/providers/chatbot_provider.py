from dishka import Provider, provide, Scope

from src.apis import ChatBotAPI
from src.repository import DialogRepository
from src.core.use_cases import ChatBotUseCase
from src.config import settings


class ChatBotProvider(Provider):
    @provide(scope=Scope.APP)
    def get_chat_bot_api(self) -> ChatBotAPI:
        return ChatBotAPI(settings.chatbot.base_url)

    @provide(scope=Scope.APP)
    def get_chat_bot_use_case(
            self,
            chat_bot_api: ChatBotAPI,
            dialog_repository: DialogRepository
    ) -> ChatBotUseCase:
        return ChatBotUseCase(chat_bot_api, dialog_repository=dialog_repository)
