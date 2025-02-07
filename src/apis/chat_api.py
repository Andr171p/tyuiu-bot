from src.http import HTTPClient
from src.apis.base import BaseAPI
from src.schemas import QuestionSchema, AnswerSchema
from src.config import settings


class ChatAPI(BaseAPI):
    _base_url = settings.chat.base_url
    _headers = settings.chat.headers
    
    async def answer_on_question(
        self, 
        question: QuestionSchema
    ) -> AnswerSchema:
        async with HTTPClient() as http_client:
            response = await http_client.post(
                url=f"{self._base_url}/chat/",
                headers=self._headers,
                data=question.model_dump()
            )
        return AnswerSchema(**response)
