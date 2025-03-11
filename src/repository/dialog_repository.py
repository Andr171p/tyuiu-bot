from typing import TYPE_CHECKING, List, Union

if TYPE_CHECKING:
    from src.database.crud import DialogCRUD

from src.repository.base_repository import BaseRepository
from src.database.models import DialogModel
from src.core.entities import Dialog
from src.dto import PerDayDistribution


class DialogRepository(BaseRepository):
    def __init__(self, crud: "DialogCRUD") -> None:
        self._crud = crud
        
    async def save(self, dialog: Dialog) -> int:
        id = await self._crud.create(DialogModel(**dialog.model_dump()))
        return id

    async def get_by_user_id(self, user_id: int) -> List[Union[Dialog, None]]:
        dialogs = await self._crud.read_by_user_id(user_id)
        return [Dialog.model_validate(dialog) for dialog in dialogs] if dialogs else []
    
    async def get_by_user_id_with_limit(
        self,
        user_id: int,
        page: int = 1,
        limit: int = 5
    ) -> List[Union[Dialog, None]]:
        dialogs = await self._crud.read_by_user_id_with_limit(
            user_id=user_id, 
            page=page, 
            limit=limit
        )
        print(dialogs)
        return [Dialog.model_validate(dialog) for dialog in dialogs] if dialogs else []
    
    async def get_all(self) -> List[Union[Dialog, None]]:
        dialogs = await self._crud.read_all()
        return [Dialog.model_validate(dialog) for dialog in dialogs] if dialogs else []
    
    async def get_count_by_user_id(self, user_id: int) -> int:
        count = await self._crud.read_count_by_user_id(user_id)
        return count if count else 0
    
    async def get_total_count(self) -> Union[int, None]:
        count = await self._crud.read_total_count()
        return count if count else 0

    async def get_count_per_day(self) -> List[PerDayDistribution]:
        per_days_count = await self._crud.read_count_per_day()
        return [PerDayDistribution(date=date, count=count) for date, count in per_days_count]
    