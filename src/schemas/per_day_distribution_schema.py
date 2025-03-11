from pydantic import BaseModel

from src.dto import PerDayDistribution


class PerDayDistributionResponse(BaseModel):
    distribution: PerDayDistribution
