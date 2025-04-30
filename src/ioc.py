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

from .settings import Settings
from .infrastructure.rest import UserRegistrationApi
from .infrastructure.telegram import TelegramSenderImpl
from .infrastructure.database.session import create_session_maker
from .infrastructure.database.repositories import SQLUserRepository, SQLContactRepository

from .core.services import UserService, NotificationService
from .core.interfaces import (
    UserRegistration,
    UserRepository,
    ContactRepository,
    TelegramSender
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
    def get_user_repository(self, session: AsyncSession) -> UserRepository:
        return SQLUserRepository(session)

    @provide(scope=Scope.REQUEST)
    def get_contact_repository(self, session: AsyncSession) -> ContactRepository:
        return SQLContactRepository(session)

    @provide(scope=Scope.APP)
    def get_user_registration(self, config: Settings) -> UserRegistration:
        return UserRegistrationApi(config.registration.url)

    @provide(scope=Scope.REQUEST)
    def get_user_service(
            self,
            user_registration: UserRegistration,
            user_repository: UserRepository,
            contact_repository: ContactRepository
    ) -> UserService:
        return UserService(
            user_registration=user_registration,
            user_repository=user_repository,
            contact_repository=contact_repository
        )

    @provide(scope=Scope.APP)
    def get_telegram_sender(self, bot: Bot) -> TelegramSender:
        return TelegramSenderImpl(bot)

    @provide(scope=Scope.APP)
    def get_notification_service(
            self,
            telegram_sender: TelegramSender,
            contact_repository: ContactRepository
    ) -> NotificationService:
        return NotificationService(
            telegram_sender=telegram_sender,
            contact_repository=contact_repository
        )


settings = Settings()

container = make_async_container(AppProvider(), context={Settings: settings})
