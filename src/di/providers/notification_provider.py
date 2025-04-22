from dishka import Provider, provide, Scope

from aiogram import Bot
from src.repository import ContactRepository
from src.services.sender import TelegramSenderService
from src.core.use_cases import NotificationUseCase
from src.controllers import NotificationController


class NotificationProvider(Provider):
    @provide(scope=Scope.APP)
    def get_sender_service(self, bot: Bot) -> TelegramSenderService:
        return TelegramSenderService(bot)

    @provide(scope=Scope.APP)
    def get_notification_use_case(
            self,
            sender_service: TelegramSenderService,
            contact_repository: ContactRepository
    ) -> NotificationUseCase:
        return NotificationUseCase(sender_service, contact_repository)

    @provide(scope=Scope.APP)
    def get_notification_controller(
            self,
            notification_use_case: NotificationUseCase
    ) -> NotificationController:
        return NotificationController(notification_use_case)
