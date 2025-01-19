from dishka import make_async_container

from src.app.providers.chat import ChatProvider


container = make_async_container(
    ChatProvider(),
)
