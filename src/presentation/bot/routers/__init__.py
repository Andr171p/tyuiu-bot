__all__ = (
    "start_router",
    "info_router",
    "chatbot_router",
    "contact_router"
)

from src.presentation.bot.routers.start import start_router
from src.presentation.bot.routers.info_router import info_router
from src.presentation.bot.routers.chat import chatbot_router
from src.presentation.bot.routers.contact_router import contact_router
