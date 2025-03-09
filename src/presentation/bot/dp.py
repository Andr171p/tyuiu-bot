from aiogram import Dispatcher
from dishka.integrations.aiogram import setup_dishka

from src.presentation.bot.routers import (
    start_router,
    info_router,
    chatbot_router
)
from src.presentation.di import container


async def create_dp() -> Dispatcher:
    dp = await container.get(Dispatcher)
    dp.include_routers(
        start_router,
        info_router,
        chatbot_router
    )
    setup_dishka(
        container=container,
        router=dp,
        auto_inject=True
    )
    return dp


dp = create_dp()
