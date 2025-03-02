


class ChatBotUseCase:
    def __init__(self, chat_bot_service: ...) -> None:
        self._chat_bot_service = chat_bot_service
        
    async def answer(self, question: str) -> str:
        ...
