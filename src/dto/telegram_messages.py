from aiogram.types import InputFile
from pydantic import BaseModel


class TelegramMessage(BaseModel):
    user_id: int
    text: str


class TelegramWithPhotoMessage(BaseModel):
    user_id: int
    photo: InputFile
    text: str
