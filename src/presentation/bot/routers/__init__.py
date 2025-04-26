__all__ = (
    "chat_router",
    "handler_router",
    "subscription_router"
)

from src.presentation.bot.routers.chat import chat_router
from src.presentation.bot.routers.handlers import handler_router
from src.presentation.bot.routers.subscription import subscription_router
