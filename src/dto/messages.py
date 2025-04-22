from typing import Literal

from pydantic import BaseModel


class UserMessageDTO(BaseModel):
    role: Literal["user"] = "user"
    chat_id: str
    text: str


class AssistantMessageDTO(BaseModel):
    role: Literal["assistant"] = "assistant"
    chat_id: str
    text: str
