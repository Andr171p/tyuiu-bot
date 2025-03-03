from dishka import make_async_container

from src.presentation.di.providers import (
    DatabaseProvider,
    RepositoryProvider,
    UsersProvider,
    ChatBotProvider,
    NotificationProvider
)


container = make_async_container(
    DatabaseProvider(),
    RepositoryProvider(),
    UsersProvider(),
    ChatBotProvider(),
    NotificationProvider()
)
