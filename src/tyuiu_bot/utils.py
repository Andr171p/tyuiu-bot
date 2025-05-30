from typing import Union

import re
import hmac
import bcrypt
import hashlib
from pathlib import Path


def read_txt(file_path: Union[Path, str]) -> str:
    with open(file_path, encoding="utf-8") as file:
        return file.read()


def format_phone_number(phone_number: str) -> str:
    """Преобразует номер телефона к формату +7(XXX)XXX-XX-XX"""
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


def get_password_hash(password: str, secret_hash_key: str) -> str:
    bytes_secret_hash_key = bytes(secret_hash_key, "utf-8")
    peppered_password = (
        hmac
        .new(bytes_secret_hash_key, password.encode("utf-8"), hashlib.sha256)
        .digest()
    )
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(peppered_password, salt)
    return hashed.decode("utf-8")
