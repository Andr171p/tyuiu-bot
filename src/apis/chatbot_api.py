from src.http import HTTPClient


class ChatBotAPI:
    def __init__(self, base_url: str) -> None:
        self._base_url = base_url
    
    async def answer(self, question: str) -> str:
        url = f"{self._base_url}/chatbot/"
        headers = {"Content-Type": "application/json; charset=UTF-8"}
        json = {"question": question}
        async with HTTPClient() as http_client:
            response = await http_client.post(
                url=url,
                headers=headers,
                json=json
            )
        return response.get("answer")
