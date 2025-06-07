from typing import Literal

from pathlib import Path


# Директория проекта:
BASE_DIR = Path(__file__).resolve().parent.parent.parent

# Переменные окружения:
ENV_PATH = BASE_DIR / ".env"

# Основной сайт:
WEBSITE_URL = "https://online-service-for-applicants.onrender.com/"

# Postgres драйверы:
POSTGRES_DRIVER: Literal["asyncpg"] = "asyncpg"

# API значения по умолчанию:
MIN_PAGE = 1
DEFAULT_PAGE = 1
DEFAULT_LIMIT = 5
DEFAULT_IS_PAGINATED = True

# Статусы пользователя:
USER_STATUS = Literal[
    "READY",
    "REGISTRATION_REQUIRE"
]

# Уровни уведомлений:
NOTIFICATION_LEVEL = Literal[
    "CHANGE_PASSWORD",  # Смена пароля
    "INFO",  # Информационный характер
    "POSITIVE",  # Положительное уведомление (призыв к подаче оригинала)
    "WARNING",  # Предупреждение
    "CRITICAL"  # Критический уровень (призыв к подаче документов на другое направление)
]

# Статусы уведомлений:
NOTIFICATION_STATUS = Literal[
    "DELIVERED",
    "NOT_DELIVERED",
    "ERROR"
]
