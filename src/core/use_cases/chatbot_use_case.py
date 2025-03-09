from typing import Optional

from src.apis import ChatBotAPI
from src.repository import DialogRepository
from src.utils import dialog_saver


class ChatBotUseCase:
    def __init__(self, chat_bot_api: ChatBotAPI, **kwargs) -> None:
        self._chat_bot_api = chat_bot_api
        self._dialog_repository: Optional[DialogRepository] = kwargs.get("dialog_repository")

    def __post_init__(self) -> None:
        self.answer = dialog_saver(self._dialog_repository)(self.answer)

    @dialog_saver(dialog_repository=None)
    async def answer(self, question: str, **kwargs) -> str:
        answer = await self._chat_bot_api.answer(question)
        return answer
