from typing import Optional

from uuid import UUID

from sqlalchemy import select
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.ext.asyncio import AsyncSession

from ..models import NotificationModel
from src.tyuiu_bot.core.dto import NotificationCreateDTO, NotificationReadDTO
from src.tyuiu_bot.core.interfaces import NotificationRepository


class SQLNotificationRepository(NotificationRepository):
    def __init__(self, session: AsyncSession) -> None:
        self.session = session

    async def create(self, notification: NotificationCreateDTO) -> None:
        try:
            notification_model = NotificationModel(**notification.model_dump())
            self.session.add(notification_model)
            await self.session.commit()
        except SQLAlchemyError as e:
            await self.session.rollback()
            raise RuntimeError(f"Error while creating notification: {e}")

    async def read(self, notification_id: UUID) -> Optional[NotificationReadDTO]:
        try:
            stmt = (
                select(NotificationModel)
                .where(NotificationModel.notification_id == notification_id)
            )
            result = await self.session.execute(stmt)
            notification = result.scalar_one_or_none()
            return NotificationReadDTO.model_validate(notification) if notification_id else None
        except SQLAlchemyError as e:
            await self.session.rollback()
            raise RuntimeError(f"Error while creating notification: {e}")

    async def get_by_user_id(self, user_id: UUID) -> list[NotificationReadDTO]:
        try:
            stmt = (
                select(NotificationModel)
                .where(NotificationModel.user_id == user_id)
            )
            results = await self.session.execute(stmt)
            notifications = results.scalars().all()
            return [NotificationReadDTO.model_validate(notification) for notification in notifications]
        except SQLAlchemyError as e:
            await self.session.rollback()
            raise RuntimeError(f"Error while creating notification: {e}")
