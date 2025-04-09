import logging

from src.http import HTTPClient
from src.apis.exceptions import APIException


log = logging.getLogger(__name__)


class AuthAPI:
    def __init__(self, base_url: str) -> None:
        self._base_url = base_url

    async def check_user_exists_by_phone_number(self, phone_number: str) -> bool:
        url = f"{self._base_url}/getnumber/{phone_number}"
        headers = {"Content-Type": "application/json; charset=UTF-8"}
        is_user_exists: bool = False
        try:
            async with HTTPClient() as http_client:
                response = await http_client.get(
                    url=url,
                    headers=headers
                )
            if response is None:
                log.warning("Service not allowed")
                return is_user_exists
            log.debug(
                "Successfully receive response %s for user with phone number %s",
                response, phone_number
            )
            is_user_exists = response["body"]
        except APIException as ex:
            log.error(ex)
            raise ex
        finally:
            return is_user_exists
