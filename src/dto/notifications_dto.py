from typing import Any

from src.core.entities import Notification


class NotificationByUserId(Notification):
    user_id: int


class NotificationByPhoneNumber(Notification):
    phone_number: str


class NotificationWithPhotoByPhoneNumber(NotificationByPhoneNumber):
    photo: Any


class NotificationWithPhotoByUserId(NotificationByUserId):
    photo: Any
