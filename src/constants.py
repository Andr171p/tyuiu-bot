from typing import Literal

from pathlib import Path

# Settings constants
BASE_DIR = Path(__file__).resolve().parent.parent
ENV_PATH = BASE_DIR / ".env"

# Endpoints constants
MIN_PAGE = 1
DEFAULT_PAGE = 1
DEFAULT_LIMIT = 5
DEFAULT_IS_PAGINATED = True

# User registration statuses:
USER_STATUSES = Literal[
    "READY",
    "REGISTRATION_REQUIRE"
]

# Notifications topics:
NOTIFICATION_TOPICS = Literal[
    "INFO",
    "POSITIVE",
    "WARNING",
    "CRITICAL"
]
NOTIFICATION_STATUSES = Literal[
    "DELIVERED",
    "ERROR"
]
