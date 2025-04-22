from typing import Literal

from pydantic import BaseModel


class AssistantMessageResponse(BaseModel):
    role: Literal["assistant"] = "assistant"
    chat_id: str
    text: str
