__all__ = (
    "wh_router",
    "admin_router",
    "statistics_router",
    "notification_router"
)

from src.app.api_v1.routers.webhook import wh_router
from src.app.api_v1.routers.admin import admin_router
from src.app.api_v1.routers.statistics import statistics_router
from src.app.api_v1.routers.notification import notification_router
