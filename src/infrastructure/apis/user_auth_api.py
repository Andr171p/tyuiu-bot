from typing import Optional


class UserAuthAPI:
    def __init__(self) -> None:
        ...

    async def is_exists(self, phone_number: str) -> Optional[dict]:
        ...
