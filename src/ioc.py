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
from src.services import TelegramSenderService
from src.infrastructure.rest import UserRegistrationApi
from src.infrastructure.database.session import create_session_maker
from src.infrastructure.database.repositories import SQLUserRepository, SQLContactRepository

from src.core.use_cases import UserManager, NotificationSender
from src.core.interfaces import SenderService, UserRegistration, UserRepository, ContactRepository


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
    def get_user_repository(self, session: AsyncSession) -> UserRepository:
        return SQLUserRepository(session)

    @provide(scope=Scope.REQUEST)
    def get_contact_repository(self, session: AsyncSession) -> ContactRepository:
        return SQLContactRepository(session)

    @provide(scope=Scope.APP)
    def get_sender_service(self, bot: Bot) -> SenderService:
        return TelegramSenderService(bot)

    @provide(scope=Scope.APP)
    def get_user_registration(self, config: Settings) -> UserRegistration:
        return UserRegistrationApi(config.user_auth.url)

    @provide(scope=Scope.REQUEST)
    def get_user_manager(
            self,
            user_registration: UserRegistration,
            user_repository: UserRepository,
            contact_repository: ContactRepository
    ) -> UserManager:
        return UserManager(
            user_registration=user_registration,
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
