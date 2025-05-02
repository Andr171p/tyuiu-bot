from ..interfaces import TelegramSender, UserRepository
from ..entities import NotificationOne, NotificationAll, NotificationBatch


class NotificationService:
    def __init__(
            self,
            telegram_sender: TelegramSender,
            user_repository: UserRepository
    ) -> None:
        self._telegram_sender = telegram_sender
        self._user_repository = user_repository

    async def notify_one(self, notification: NotificationOne) -> None:
        user_id = notification.user_id
        phone_number = notification.phone_number
        content = notification.content
        if user_id:
            telegram_id = await self._user_repository.get_telegram_id_by_user_id(user_id)
        else:
            telegram_id = await self._user_repository.get_telegram_id_by_phone_number(phone_number)
        await self._telegram_sender.send(
            telegram_id=telegram_id,
            text=content.text,
            image_url=content.image_url,
            image_base64=content.image_base64
        )

    async def notify_all(self, notification: NotificationAll) -> None:
        content = notification.content
        users = await self._user_repository.list()
        for user in users:
            await self._telegram_sender.send(
                telegram_id=user.telegram_id,
                text=content.text,
                image_url=content.image_url,
                image_base64=content.image_base64
            )

    async def notify_batch(self, notification: NotificationBatch) -> None:
        phone_numbers = notification.phone_numbers
        user_ids = notification.user_ids
        content = notification.content
        if phone_numbers:
            users = await self._user_repository.get_by_phone_numbers(phone_numbers)
        else:
            users = await self._user_repository.get_by_user_ids(user_ids)
        for user in users:
            await self._telegram_sender.send(
                telegram_id=user.telegram_id,
                text=content.text,
                image_url=content.image_url,
                image_base64=content.image_base64
            )
