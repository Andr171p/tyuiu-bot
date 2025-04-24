from dishka import Provider, provide, Scope, from_context

from src.settings import Settings
from src.repository import UserRepository, ContactRepository
from src.core.use_cases import ChatAssistant, UserManager, NotificationSender
from src.core.interfaces import (
    AbstractChatAssistantGateway,
    AbstractUserAuthGateway,
    AbstractSenderService
)


class AppProvider(Provider):
    settings = from_context(provides=Settings, scope=Scope.APP)

    @provide(scope=Scope.APP)
    def get_chat_assistant(self, chat_assistant_gateway: AbstractChatAssistantGateway) -> ChatAssistant:
        return ChatAssistant(chat_assistant_gateway)

    @provide(scope=Scope.REQUEST)
    def get_user_manager(
            self,
            user_auth_gateway: AbstractUserAuthGateway,
            user_repository: UserRepository,
            contact_repository: ContactRepository
    ) -> UserManager:
        return UserManager(
            user_auth_gateway=user_auth_gateway,
            user_repository=user_repository,
            contact_repository=contact_repository
        )

    @provide(scope=Scope.REQUEST)
    def get_notification_sender(
            self,
            sender_service: AbstractSenderService,
            contact_repository: ContactRepository
    ) -> NotificationSender:
        return NotificationSender(sender_service, contact_repository)
