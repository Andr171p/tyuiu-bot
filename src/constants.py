from typing import Literal

from pathlib import Path

# Settings constants
BASE_DIR = Path(__file__).resolve().parent.parent
ENV_PATH = BASE_DIR / ".env"

# Main web site:
SITE_URL = "https://online-service-for-applicants.onrender.com/"

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

# Notifications:
NOTIFICATION_LEVELS = Literal[
    "INFO",
    "POSITIVE",
    "WARNING",
    "CRITICAL"
]  # Notification topics level
NOTIFICATION_STATUSES = Literal[
    "DELIVERED",
    "NOT_DELIVERED",
    "ERROR"
]
