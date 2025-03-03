from typing import Callable, Coroutine, Any
from datetime import datetime
from functools import wraps

from src.core.entities import Chat
from src.repository import ChatRepository


def chat_saver(chat_repository: ChatRepository):
    def decorator(func: Callable[..., Coroutine[Any, Any, str]]):
        @wraps(func)
        async def wrapper(self, user_id: int, question: str, *args, **kwargs) -> str:
            answer = await func(self, user_id, question, *args, **kwargs)
            chat = Chat(
                user_id=user_id,
                user_message=question,
                chat_bot_message=answer,
                created_at=datetime.now()
            )
            await chat_repository.save(chat)
            return answer
        return wrapper
    return decorator
