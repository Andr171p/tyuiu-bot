from typing import Optional

from datetime import datetime
from uuid import UUID

from .entities import User, Notification
from ..constants import NOTIFICATION_STATUSES


class UserReadDTO(User):
    created_at: datetime
    updated_at: datetime


class NotificationCreateDTO(Notification):
    status: NOTIFICATION_STATUSES
    message_id: Optional[int]


class NotificationReadDTO(Notification):
    notification_id: UUID
    status: NOTIFICATION_STATUSES
    created_at: datetime
