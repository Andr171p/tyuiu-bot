from typing import Dict
from collections import defaultdict

from src.repository.base import BaseRepository
from src.misc.formaters import format_to_year_month_day


async def get_count(repository: BaseRepository) -> int:
    items = await repository.get_all()
    if items is None:
        return 0
    return len(items)


async def get_count_per_day(repository: BaseRepository) -> Dict[str, int]:
    items = await repository.get_all()
    date_to_count_dict = defaultdict(int)
    for item in items:
        date = format_to_year_month_day(item.created_at)
        date_to_count_dict[date] += 1
    return dict(date_to_count_dict)
