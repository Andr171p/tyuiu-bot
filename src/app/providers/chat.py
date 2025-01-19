from dishka import Provider, Scope, provide

from src.services.chat import ChatService


class ChatProvider(Provider):
    @provide(scope=Scope.APP)
    def get_chat_api_service(self) -> ChatService:
        return ChatService()
