from typing import List

from pydantic import BaseModel

from src.dto import PerDayDistribution


class PerDayDistributionResponse(BaseModel):
    distribution: List[PerDayDistribution]
