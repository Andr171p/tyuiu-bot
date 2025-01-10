from src.core.http import HTTPClient
from src.schemas import ResponseSchema

from src.config import settings


class RAGAPIService:
    def __init__(
            self,
            base_url: str = settings.api.base_url
    ) -> None:
        self._base_url = base_url

    async def get_answer(self, query: str) -> ResponseSchema:
        async with HTTPClient() as http_client:
            response = await http_client.get(
                url=f"{self._base_url}/rag/answer/?query={query}"
            )
        return ResponseSchema.parse_obj(response)
