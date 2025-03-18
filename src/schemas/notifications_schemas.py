from pydantic import BaseModel
from fastapi import UploadFile


class NotificationALLWithPhotoSchema(BaseModel):
    text: str
    photo: UploadFile


class NotificationWithPhotoByPhoneNumberSchema(BaseModel):
    text: str
    photo: UploadFile
    phone_number: str
