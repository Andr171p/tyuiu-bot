from typing import Literal

from pathlib import Path


# Директория проекта:
BASE_DIR = Path(__file__).resolve().parent.parent.parent

# Переменные окружения:
ENV_PATH = BASE_DIR / ".env"

# Main web site:
SITE_URL = "https://online-service-for-applicants.onrender.com/"

# API значения по умолчанию:
MIN_PAGE = 1
DEFAULT_PAGE = 1
DEFAULT_LIMIT = 5
DEFAULT_IS_PAGINATED = True

# Статусы пользователя:
USER_STATUSES = Literal[
    "READY",
    "REGISTRATION_REQUIRE"
]

# Уровни уведомлений:
NOTIFICATION_LEVELS = Literal[
    "INFO",  # Информационный характер
    "POSITIVE",  # Положительное уведомление (призыв к подаче оригинала)
    "WARNING",  # Предупреждение
    "CRITICAL"  # Критический уровень (призыв к подаче документов на другое направление)
]
# Статусы уведомлений:
NOTIFICATION_STATUSES = Literal[
    "DELIVERED",
    "NOT_DELIVERED",
    "ERROR"
]
