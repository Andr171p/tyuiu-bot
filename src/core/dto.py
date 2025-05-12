from datetime import datetime

from .entities import User, Notification
from ..constants import NOTIFICATION_STATUSES


class UserReadDTO(User):
    created_at: datetime


class NotificationCreateDTO(Notification):
    status: NOTIFICATION_STATUSES
    message_id: int


class NotificationReadDTO(Notification):
    status: NOTIFICATION_STATUSES
    created_at: datetime
