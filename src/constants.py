from pathlib import Path

"""Settings constants"""
BASE_DIR = Path(__file__).resolve().parent.parent
ENV_PATH = BASE_DIR / ".env"

"""Endpoints constants"""
GE_PAGINATED = 1
DEFAULT_PAGE = 1
DEFAULT_LIMIT = 5
DEFAULT_IS_PAGINATED = True
