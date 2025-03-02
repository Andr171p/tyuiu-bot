from datetime import datetime

from src.apis import ChatBotAPI
from src.repository import DialogRepository
from src.core.entities import Dialog


class ChatBotUseCase:
    def __init__(
        self, 
        chat_bot_api: ChatBotAPI,
        dialog_repository: DialogRepository
    ) -> None:
        self._chat_bot_api = chat_bot_api
        self._dialog_repository = dialog_repository
        
    async def answer(self, user_id: int, question: str) -> str:
        answer = self._chat_bot_api.answer(question)
        dialog = Dialog(
            user_id=user_id,
            user_message=question,
            chat_bot_message=answer,
            created_at=datetime.now()
        )
        await self._dialog_repository.add(dialog)
        return answer
