import re
from datetime import datetime


def format_phone_number(phone_number: str) -> str:
    digits = re.sub(
        pattern='\D',
        repl='',
        string=phone_number
    )
    if len(digits) == 11 and digits.startswith('8'):
        digits = '7' + digits[1:]
    elif len(digits) == 10 and digits.startswith('9'):
        digits = '7' + digits
    return f"+{digits[0]}({digits[1:4]}){digits[4:7]}-{digits[7:9]}-{digits[9:11]}"


def format_to_year_month_day(date: datetime) -> str:
    return date.strftime("%Y-%m-%d")
