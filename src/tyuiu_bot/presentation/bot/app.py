from aiogram import Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage

from dishka.integrations.aiogram import setup_dishka

from src.tyuiu_bot.ioc import container
from .handler import router


def create_aiogram_app() -> Dispatcher:
    dispatcher = Dispatcher(storage=MemoryStorage())
    dispatcher.include_routers(router)
    setup_dishka(container=container, router=dispatcher, auto_inject=True)
    return dispatcher


dp = create_aiogram_app()
