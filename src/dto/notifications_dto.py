from fastapi import UploadFile
from pydantic import BaseModel


class NotificationAllWithPhotoDTO(BaseModel):
    text: str
    photo: UploadFile


class NotificationWithPhotoByPhoneNumberDTO(BaseModel):
    text: str
    photo: UploadFile
    phone_number: str
