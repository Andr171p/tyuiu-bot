from typing import Callable, Coroutine, Any, Optional
from datetime import datetime
from functools import wraps

from src.core.entities import Chat
from src.repository import ChatRepository


def chat_saver(chat_repository: Optional[ChatRepository]):
    def decorator(func: Callable[..., Coroutine[Any, Any, str]]):
        @wraps(func)
        async def wrapper(self, question: str, *args, **kwargs) -> str:
            user_id = kwargs.get("user_id")  # Извлекаем user_id из kwargs
            if user_id is None:
                raise ValueError("user_id is required")

            answer = await func(self, question, *args, **kwargs)
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
