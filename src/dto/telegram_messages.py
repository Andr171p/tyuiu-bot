from pydantic import BaseModel


class TelegramMessage(BaseModel):
    user_id: int
    text: str


class TelegramWithPhotoMessage(BaseModel):
    user_id: int
    photo: str
    text: str
