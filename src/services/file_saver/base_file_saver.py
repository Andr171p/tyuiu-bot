from abc import ABC, abstractmethod


class BaseFileSaver(ABC):
    @abstractmethod
    async def save(self, *args) -> str:
        raise NotImplemented
