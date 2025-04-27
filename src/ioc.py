from typing import AsyncIterable

from dishka import (
    Provider,
    provide,
    Scope,
    from_context,
    make_async_container
)

from aiogram import Bot
from aiogram.enums.parse_mode import ParseMode
from aiogram.client.default import DefaultBotProperties

from faststream.rabbit import RabbitBroker

from sqlalchemy.ext.asyncio import async_sessionmaker, AsyncSession

from src.settings import Settings
from src.infrastructure.database.crud import UserCRUD, ContactCRUD
from src.infrastructure.database.session import create_session_maker
from src.repositories import UserRepositoryImpl, ContactRepositoryImpl

from src.infrastructure.apis import UserAuthAPI
from src.services import TelegramSenderService
from src.gateways import ChatAssistantRabbitGateway, UserAuthAPIGateway

from src.core.use_cases import ChatAssistant, UserManager, NotificationSender
from src.core.interfaces import (
    ChatAssistantGateway,
    SenderService,
    UserAuthGateway,
    UserRepository,
    ContactRepository
)


class AppProvider(Provider):
    config = from_context(provides=Settings, scope=Scope.APP)

    @provide(scope=Scope.APP)
    def get_bot(self, config: Settings) -> Bot:
        return Bot(
            token=config.bot.token,
            default=DefaultBotProperties(parse_mode=ParseMode.HTML)
        )

    @provide(scope=Scope.APP)
    def get_rabbit_broker(self, config: Settings) -> RabbitBroker:
        return RabbitBroker(url=config.rabbit.url)

    @provide(scope=Scope.APP)
    def get_session_maker(self, config: Settings) -> async_sessionmaker[AsyncSession]:
        return create_session_maker(config.postgres)

    @provide(scope=Scope.REQUEST)
    async def get_session(self, session_maker: async_sessionmaker[AsyncSession]) -> AsyncIterable[AsyncSession]:
        async with session_maker() as session:
            yield session

    @provide(scope=Scope.REQUEST)
    def get_user_crud(self, session: AsyncSession) -> UserCRUD:
        return UserCRUD(session)

    @provide(scope=Scope.REQUEST)
    def get_contact_crud(self, session: AsyncSession) -> ContactCRUD:
        return ContactCRUD(session)

    @provide(scope=Scope.REQUEST)
    def get_user_repository(self, crud: UserCRUD) -> UserRepository:
        return UserRepositoryImpl(crud)

    @provide(scope=Scope.REQUEST)
    def get_contact_repository(self, crud: ContactCRUD) -> ContactRepository:
        return ContactRepositoryImpl(crud)

    @provide(scope=Scope.APP)
    def get_sender_service(self, bot: Bot) -> SenderService:
        return TelegramSenderService(bot)

    @provide(scope=Scope.APP)
    def get_user_auth_api(self, config: Settings) -> UserAuthAPI:
        return UserAuthAPI(config.user_auth.url)

    @provide(scope=Scope.APP)
    def get_user_auth_gateway(self, user_auth_api: UserAuthAPI) -> UserAuthGateway:
        return UserAuthAPIGateway(user_auth_api)

    @provide(scope=Scope.APP)
    def get_chat_assistant_gateway(self, broker: RabbitBroker) -> ChatAssistantGateway:
        return ChatAssistantRabbitGateway(broker)

    @provide(scope=Scope.APP)
    def get_chat_assistant(self, chat_assistant_gateway: ChatAssistantGateway) -> ChatAssistant:
        return ChatAssistant(chat_assistant_gateway)

    @provide(scope=Scope.REQUEST)
    def get_user_manager(
            self,
            user_auth_gateway: UserAuthGateway,
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
            sender_service: SenderService,
            contact_repository: ContactRepository
    ) -> NotificationSender:
        return NotificationSender(sender_service, contact_repository)


settings = Settings()

container = make_async_container(AppProvider(), context={Settings: settings})
