from dishka import Provider, provide, Scope

from src.infrastructure.apis import ChatBotAPI
from src.repository import DialogRepository
from src.core.use_cases import ChatBotUseCase
from src.controllers import ChatBotController
from src.settings import settings


class ChatBotProvider(Provider):
    @provide(scope=Scope.APP)
    def get_chat_bot_api(self) -> ChatBotAPI:
        return ChatBotAPI(settings.chatbot.base_url)

    @provide(scope=Scope.APP)
    def get_chat_bot_use_case(
            self,
            chatbot_api: ChatBotAPI,
            dialog_repository: DialogRepository
    ) -> ChatBotUseCase:
        return ChatBotUseCase(
            chatbot_api=chatbot_api,
            dialog_repository=dialog_repository
        )

    @provide(scope=Scope.APP)
    def get_chatbot_controller(self, chatbot_use_case: ChatBotUseCase) -> ChatBotController:
        return ChatBotController(chatbot_use_case)
