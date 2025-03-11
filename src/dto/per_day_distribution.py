from datetime import datetime

from pydantic import BaseModel


class PerDayDistribution(BaseModel):
    date: datetime
    count: int
