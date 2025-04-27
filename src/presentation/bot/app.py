from aiogram import Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage
from dishka.integrations.aiogram import setup_dishka

from src.presentation.bot.routers import (
    chat_router,
    handler_router,
    subscription_router
)
from src.ioc import container


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
