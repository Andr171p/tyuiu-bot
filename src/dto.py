from datetime import datetime

from pydantic import BaseModel


class DailyCount(BaseModel):
    date: datetime
    count: int
