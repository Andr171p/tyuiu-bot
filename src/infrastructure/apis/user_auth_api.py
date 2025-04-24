from typing import Optional


class UserAuthAPI:
    def __init__(self, base_url: str) -> None:
        self._base_url = base_url

    async def is_exists(self, phone_number: str) -> Optional[dict]:
        ...
