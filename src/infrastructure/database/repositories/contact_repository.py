from datetime import datetime

from collections.abc import Sequence
from typing import List, Tuple, Optional

from sqlalchemy import select, func
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.ext.asyncio import AsyncSession

from ..models import ContactModel
from src.core.interfaces import ContactRepository
from src.core.entities import Contact, CreatedContact


class SQLContactRepository(ContactRepository):
    def __init__(self, session: AsyncSession) -> None:
        self.session = session

    async def create(self, contact: Contact) -> CreatedContact:
        try:
            contact_model = ContactModel.from_contact(contact)
            self.session.add(contact_model)
            await self.session.flush()
            await self.session.commit()
            return CreatedContact.model_validate(contact_model)
        except SQLAlchemyError as ex:
            await self.session.rollback()
            raise RuntimeError(f"Error while creating contact: {ex}")

    async def read(self, telegram_id: int) -> Optional[CreatedContact]:
        try:
            stmt = (
                select(ContactModel)
                .where(ContactModel.telegram_id == telegram_id)
            )
            result = await self.session.execute(stmt)
            contact = result.scalar_one_or_none()
            return CreatedContact.model_validate(contact) if contact else None
        except SQLAlchemyError as ex:
            await self.session.rollback()
            raise RuntimeError(f"Error while reading contact: {ex}")

    async def get_by_phone_number(self, phone_number: str) -> Optional[CreatedContact]:
        try:
            stmt = (
                select(ContactModel)
                .where(ContactModel.phone_number == phone_number)
            )
            result = await self.session.execute(stmt)
            contact = result.scalar_one_or_none()
            return CreatedContact.model_validate(contact) if contact else None
        except SQLAlchemyError as ex:
            await self.session.rollback()
            raise RuntimeError(f"Error while reading by phone_number: {ex}")

    async def get_telegram_id_by_phone_number(self, phone_number: str) -> int:
        try:
            stmt = (
                select(ContactModel.telegram_id)
                .where(ContactModel.phone_number == phone_number)
            )
            telegram_id = await self.session.execute(stmt)
            return telegram_id.scalar()
        except SQLAlchemyError as ex:
            await self.session.rollback()
            raise RuntimeError(f"Error while reading telegram_id by phone_number: {ex}")

    async def get_phone_number_by_telegram_id(self, telegram_id: int) -> str:
        try:
            stmt = (
                select(ContactModel.phone_number)
                .where(ContactModel.telegram_id == telegram_id)
            )
            phone_number = await self.session.execute(stmt)
            return phone_number.scalar()
        except SQLAlchemyError as ex:
            await self.session.rollback()
            raise RuntimeError(f"Error while reading phone_number by telegram_id: {ex}")

    async def get_registered(self, is_registered: bool = True) -> List[Optional[CreatedContact]]:
        try:
            stmt = (
                select(ContactModel)
                .where(ContactModel.is_registered == is_registered)
            )
            results = await self.session.execute(stmt)
            contacts = results.scalars().all()
            return [CreatedContact.model_validate(contact) for contact in contacts] if contacts else []
        except SQLAlchemyError as ex:
            await self.session.rollback()
            raise RuntimeError(f"Error while reding registered users: {ex}")

    async def list(self) -> List[CreatedContact]:
        try:
            stmt = select(ContactModel)
            results = await self.session.execute(stmt)
            contacts = results.scalars().all()
            return [CreatedContact.model_validate(contact) for contact in contacts]
        except SQLAlchemyError as ex:
            await self.session.rollback()
            raise RuntimeError(f"Error while reading contacts: {ex}")

    async def list_of_telegram_ids(self) -> Sequence[int]:
        try:
            stmt = select(ContactModel.telegram_id)
            user_ids = await self.session.execute(stmt)
            return user_ids.scalars().all()
        except SQLAlchemyError as ex:
            await self.session.rollback()
            raise RuntimeError(f"Error while reading telegram ids: {ex}")

    async def paginate(self, page: int, limit: int) -> List[Optional[CreatedContact]]:
        try:
            offset = (page - 1) * limit
            stmt = (
                select(ContactModel)
                .offset(offset)
                .limit(limit)
            )
            results = await self.session.execute(stmt)
            contacts = results.scalars().all()
            return [CreatedContact.model_validate(contact) for contact in contacts] if contacts else []
        except SQLAlchemyError as ex:
            await self.session.rollback()
            raise RuntimeError(f"Error while reading paginated contacts: {ex}")

    async def count(self) -> int:
        try:
            stmt = (
                select(func.count())
                .select_from(ContactModel)
            )
            count = await self.session.execute(stmt)
            return count.scalar()
        except SQLAlchemyError as ex:
            await self.session.rollback()
            raise RuntimeError(f"Error while reading count contacts: {ex}")

    async def count_daily(self) -> Sequence[Tuple[datetime, int]]:
        try:
            stmt = (
                select(
                    func.date(ContactModel.created_at).label("date"),
                    func.count().label("count")
                )
                .group_by(func.date(ContactModel.created_at))
                .order_by(func.date(ContactModel.created_at))
            )
            count = await self.session.execute(stmt)
            return count.scalars().all()
        except SQLAlchemyError as ex:
            await self.session.rollback()
            raise RuntimeError(f"Error while reading count daily: {ex}")
