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
    dp = Dispatcher(storage=MemoryStorage())
    dp.include_routers(
        chat_router,
        handler_router,
        subscription_router
    )
    setup_dishka(
        container=container,
        router=dp,
        auto_inject=True
    )
    return dp


dp = create_aiogram_app()
