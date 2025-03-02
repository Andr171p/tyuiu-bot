from typing import TYPE_CHECKING, Optional

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
            headers: Optional[dict] = None,
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
            json: dict,
            headers: Optional[dict] = None
    ) -> dict | None:
        async with self._session.post(
            url=url,
            json=json,
            headers=headers
        ) as response:
            if self.is_ok(response):
                return await response.json()
