from typing import Any, Optional
from abc import ABC, abstractmethod


class AbstractSenderService(ABC):
    @abstractmethod
    async def send(
            self,
            user_id: int,
            text: str,
            photo: Optional[Any] = None,
    ) -> bool:
        raise NotImplemented
