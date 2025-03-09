from dishka import Provider, provide, Scope

from aiogram import Bot  # Dispatcher
from aiogram.enums.parse_mode import ParseMode
from aiogram.client.default import DefaultBotProperties
# from aiogram.fsm.storage.memory import MemoryStorage

from src.config import settings


class BotProvider(Provider):
    @provide(scope=Scope.APP)
    def get_bot(self) -> Bot:
        return Bot(
            token=settings.bot.token,
            parse_mode=DefaultBotProperties(parse_mode=ParseMode.HTML)
        )

    '''
    @provide(scope=Scope.APP)
    def get_dp(self) -> Dispatcher:
        return Dispatcher(storage=MemoryStorage())
    '''
