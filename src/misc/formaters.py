from datetime import datetime


def format_to_year_month_day(date: datetime) -> str:
    # date = datetime.strptime(date, "%Y-%m-%d %H:%M:%S")
    return date.strftime("%Y-%m-%d")
