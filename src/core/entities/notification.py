from pydantic import BaseModel


class Notification(BaseModel):
    text: str
