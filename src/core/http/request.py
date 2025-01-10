from typing import (
    TYPE_CHECKING
)

if TYPE_CHECKING:
    from aiohttp import ClientSession, ClientResponse


class HTTPRequests:
    _session: "ClientSession"

    @staticmethod
    def is_ok(response: "ClientResponse") -> bool:
        return 200 <= response.status < 300

    async def get(
            self,
            url: str,
            headers: dict = None,
            timeout: int = 10
    ) -> dict | None:
        async with self._session.get(
            url=url,
            headers=headers,
            timeout=timeout
        ) as response:
            if self.is_ok(response):
                return await response.json()

    async def post(
            self,
            url: str,
            data: dict,
            headers: dict = None
    ) -> dict | None:
        async with self._session.post(
            url=url,
            json=data,
            headers=headers
        ) as response:
            if self.is_ok(response):
                return await response.json()
