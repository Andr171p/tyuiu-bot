from dishka import make_async_container

from src.app.providers import (
    ChatProvider,
    AnalyticsProvider,
    NotificationProvider
)


container = make_async_container(
    ChatProvider(),
    AnalyticsProvider(),
    NotificationProvider()
)
