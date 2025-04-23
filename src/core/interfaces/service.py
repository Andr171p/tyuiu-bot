from typing import Optional
from abc import ABC, abstractmethod


class AbstractSenderService(ABC):
    @abstractmethod
    async def send(
            self,
            user_id: int,
            text: str,
            photo_url: Optional[str] = None,
            photo_base64: Optional[str] = None
    ) -> bool:
        raise NotImplemented
