from typing import Optional
from abc import ABC


class BaseAPI(ABC):
    _base_url: Optional[str] = None
    _headers: Optional[dict] = None
