from aiogram import Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage
from dishka.integrations.aiogram import setup_dishka

from src.ioc import container
from .routers import (
    chat_router,
    handler_router,
    subscription_router
)


def create_aiogram_app() -> Dispatcher:
    dispatcher = Dispatcher(storage=MemoryStorage())
    dispatcher.include_routers(
        handler_router,
        subscription_router,
        chat_router
    )
    setup_dishka(
        container=container,
        router=dispatcher,
        auto_inject=True
    )
    return dispatcher


dp = create_aiogram_app()
