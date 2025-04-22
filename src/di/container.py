from dishka import make_async_container

from src.di.providers import (
    DatabaseProvider,
    BotProvider,
    RepositoryProvider,
    UsersProvider,
    ChatBotProvider,
    NotificationProvider,
    ChatsProvider
)


container = make_async_container(
    DatabaseProvider(),
    BotProvider(),
    RepositoryProvider(),
    UsersProvider(),
    ChatBotProvider(),
    NotificationProvider(),
    ChatsProvider()
)
