from typing import Callable, Coroutine, Any, Optional
from datetime import datetime
from functools import wraps

from src.core.entities import Dialog
from src.repository import DialogRepository


def dialog_saver(dialog_repository: Optional[DialogRepository]):
    def decorator(func: Callable[..., Coroutine[Any, Any, str]]):
        @wraps(func)
        async def wrapper(self, question: str, *args, **kwargs) -> str:
            user_id = kwargs.get("user_id")
            if user_id is None:
                raise ValueError("user_id is required")
            answer = await func(self, question, *args, **kwargs)
            dialog = Dialog(
                user_id=user_id,
                user_message=question,
                chat_bot_message=answer,
                created_at=datetime.now()
            )
            await dialog_repository.save(dialog)
            return answer
        return wrapper
    return decorator
