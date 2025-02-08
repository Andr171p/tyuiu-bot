from dishka import make_async_container

from src.app.providers import (
    UserServiseProvider,
    ChatServiceProvider,
    NotificationServiceProvider
)


container = make_async_container(
    UserServiseProvider(),
    ChatServiceProvider(),
    NotificationServiceProvider()
)
