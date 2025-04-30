from typing import Optional
from abc import ABC, abstractmethod


class TelegramSender(ABC):
    @abstractmethod
    async def send(
            self,
            telegram_id: int,
            text: str,
            image_url: Optional[str],
            image_base64: Optional[str]
    ) -> bool: pass
