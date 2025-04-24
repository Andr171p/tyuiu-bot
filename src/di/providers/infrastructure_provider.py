from dishka import Provider, provide, Scope

from aiogram import Bot
from aiogram.enums.parse_mode import ParseMode
from aiogram.client.default import DefaultBotProperties

from faststream.rabbit import RabbitBroker

from src.core.interfaces import AbstractChatAssistantGateway

from src.infrastructure.apis import UserAuthAPI
from src.gateways.chat_assistant import ChatAssistantRabbitGateway

from src.settings import Settings


class InfrastructureProvider(Provider):
    @provide(scope=Scope.APP)
    def get_bot(self, settings: Settings) -> Bot:
        return Bot(
            token=settings.bot.token,
            default=DefaultBotProperties(parse_mode=ParseMode.HTML)
        )

    @provide(scope=Scope.APP)
    def get_rabbit_broker(self, settings: Settings) -> RabbitBroker:
        return RabbitBroker(url=settings.rabbit.url)

    @provide(scope=Scope.APP)
    def get_user_auth_api(self, settings: Settings) -> UserAuthAPI:
        return UserAuthAPI(settings.auth.base_url)

    @provide(scope=Scope.APP)
    def get_chat_assistant_rabbit_gateway(self, broker: RabbitBroker) -> AbstractChatAssistantGateway:
        return ChatAssistantRabbitGateway(broker)
