import logging
from typing import Union

from src.http import HTTPClient
from src.apis.exceptions import APIException


log = logging.getLogger(__name__)


class AuthAPI:
    def __init__(self, base_url: str) -> None:
        self._base_url = base_url

    async def check_user_exists_by_phone_number(self, phone_number: str) -> Union[bool, None]:
        url = f"{self._base_url}/getnumber/{phone_number}"
        headers = {"Content-Type": "application/json; charset=UTF-8"}
        try:
            async with HTTPClient() as http_client:
                response = await http_client.get(
                    url=url,
                    headers=headers
                )
            message = response.get("message")
            log.debug(
                "Successfully receive message %s for user with phone number %s",
                message, phone_number
            )
            return ...
        except APIException as ex:
            log.error(ex)
            raise ex
