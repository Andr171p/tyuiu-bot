import logging
from typing import Union

from src.http import HTTPClient
from src.apis.exceptions import APIException


log = logging.getLogger(__name__)


class ChatBotAPI:
    def __init__(self, base_url: str) -> None:
        self._base_url = base_url
    
    async def answer(self, question: str) -> Union[str, None]:
        url = f"{self._base_url}/chatbot/"
        headers = {"Content-Type": "application/json; charset=UTF-8"}
        json = {"question": question}
        try:
            async with HTTPClient() as http_client:
                response = await http_client.post(
                    url=url,
                    headers=headers,
                    json=json
                )
            answer = response.get("answer")
            log.debug(
                "Successfully receive answer %s on question %s",
                answer, question
            )
            return answer
        except APIException as ex:
            log.error(ex)
            raise ex
