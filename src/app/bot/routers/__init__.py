__all__ = (
    "start_router",
    "info_router",
    "notification_router",
    "chat_router"
)

from src.app.bot.routers.start import start_router
from src.app.bot.routers.info import info_router
from src.app.bot.routers.notification import notification_router
from src.app.bot.routers.chat import chat_router
