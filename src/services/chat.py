import logging
from typing import List

from src.apis import ChatAPI
from src.repository import MessageRepository
from src.schemas import (
    QuestionSchema, 
    MessageSchema,
    PaginatedMessagesSchema
)


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
        
    async def get_messages_history_by_user_id(
        self, 
        user_id: int
    ) -> List[MessageSchema] | None:
        messages = await self._message_repository.get_by_user_id(user_id)
        log.info(
            "Messages history %s for user %s retrieved successfully", 
            len(messages),
            user_id
        )
        return messages
    
    async def get_paginated_messages_history_by_user_id(
        self,
        user_id: int,
        page: int = 1,
        limit: int = 5
    ) -> PaginatedMessagesSchema | None:
        messages = await self._message_repository.get_by_user_id_with_limit(
            user_id=user_id,
            page=page,
            limit=limit
        )
        total_messages_count = await self._message_repository.get_count_by_user_id(
            user_id=user_id
        )
        log.info(
            "Successfully retrieved %s messages for user %s", 
            total_messages_count, 
            user_id
        )
        return PaginatedMessagesSchema(
            user_id=user_id,
            total=total_messages_count,
            page=page,
            limit=limit,
            messages=messages
        )
