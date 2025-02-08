import logging

from src.apis import ChatAPI
from src.repository import MessageRepository
from src.schemas import QuestionSchema, MessageSchema


log = logging.getLogger(__name__)


class ChatService:
    _chat_api = ChatAPI()
    _message_repository = MessageRepository()
    
    async def answer_on_question(self, question: str) -> str:
        chat_question = QuestionSchema(question=question)
        chat_answer = await self._chat_api.answer_on_question(chat_question)
        log.info("Answer recieved successfully")
        return chat_answer.answer
    
    async def save_dialog(self, message: MessageSchema) -> None:
        saved_message = await self._message_repository.add(message)
        log.info("Message %s message saved successfully", saved_message)
        
