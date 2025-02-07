from src.apis import ChatAPI
from src.schemas import QuestionSchema


class ChatService:
    _chat_api = ChatAPI()
    
    async def answer_on_question(self, question: str) -> str:
        chat_question = QuestionSchema(question=question)
        chat_answer = await self._chat_api.answer_on_question(chat_question)
        return chat_answer.answer
