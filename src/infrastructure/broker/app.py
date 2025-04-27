from faststream import FastStream
from faststream.rabbit import RabbitBroker
from dishka.integrations.faststream import setup_dishka

from src.ioc import container
from src.infrastructure.broker.routers import chat_router, notifications_router


async def create_faststream_app() -> FastStream:
    broker = await container.get(RabbitBroker)
    broker.include_routers(chat_router, notifications_router)
    app = FastStream(broker)
    setup_dishka(
        container=container,
        app=app,
        auto_inject=True
    )
    return app
