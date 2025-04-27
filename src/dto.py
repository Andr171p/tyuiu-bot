from datetime import datetime

from pydantic import BaseModel


class CreationDateCountDTO(BaseModel):
    date: datetime
    count: int
