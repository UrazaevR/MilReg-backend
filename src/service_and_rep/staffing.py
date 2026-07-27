from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from src.models.staffing import StaffingTable
from src.schemas.staffing import StaffingCreate, StaffingUpdate
from .base import BaseRepository
import uuid
from typing import Optional, List

class StaffingRepository(BaseRepository[StaffingTable, StaffingCreate, StaffingUpdate]):
    def __init__(self, db: AsyncSession):
        super().__init__(StaffingTable, db)

    async def get_by_department(self, department_id: uuid.UUID) -> List[StaffingTable]:
        """Получить все штатные единицы по ID подразделения."""
        result = await self.db.execute(
            select(StaffingTable).where(StaffingTable.department_id == department_id)
        )
        return result.scalars().all()

    async def get_by_name(self, name: str) -> Optional[StaffingTable]:
        """Найти штатную единицу по названию (точное совпадение)."""
        result = await self.db.execute(
            select(StaffingTable).where(StaffingTable.name == name)
        )
        return result.scalar_one_or_none()