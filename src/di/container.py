from dishka import make_async_container

from src.di.providers import (
    AppProvider,
    DatabaseProvider,
    InfrastructureProvider
)
from src.settings import Settings


settings = Settings()

container = make_async_container(
    InfrastructureProvider(),
    DatabaseProvider(),
    AppProvider(),
    context={Settings: settings}
)
