from typing import AsyncIterable

from dishka import Provider, provide, Scope

from sqlalchemy.ext.asyncio import async_sessionmaker, AsyncSession

from src.infrastructure.database.session import create_session_maker
from src.infrastructure.database.crud import UserCRUD, ContactCRUD
from src.repository import UserRepository, ContactRepository
from src.settings import Settings


class DatabaseProvider(Provider):
    @provide(scope=Scope.APP)
    def get_session_maker(self, settings: Settings) -> async_sessionmaker[AsyncSession]:
        return create_session_maker(settings.postgres)

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
        return UserRepository(crud)

    @provide(scope=Scope.REQUEST)
    def get_contact_repository(self, crud: ContactCRUD) -> ContactRepository:
        return ContactRepository(crud)
