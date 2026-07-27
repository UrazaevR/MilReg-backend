from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from src.models.person import Person
from src.schemas.person import PersonCreate, PersonUpdate
from .base import BaseRepository
import uuid
from typing import Optional

class PersonRepository(BaseRepository[Person, PersonCreate, PersonUpdate]):
    def __init__(self, db: AsyncSession):
        super().__init__(Person, db)

    # Дополнительные методы
    async def get_by_snils(self, snils: str) -> Optional[Person]:
        result = await self.db.execute(
            select(Person).where(Person.snils == snils)
        )
        return result.scalar_one_or_none()

    async def get_by_inn(self, inn: str) -> Optional[Person]:
        result = await self.db.execute(
            select(Person).where(Person.inn == inn)
        )
        return result.scalar_one_or_none()

    # Получить всех сотрудников определённого отдела (через staffing)
    async def get_by_department_id(self, department_id: uuid.UUID) -> list[Person]:
        # Сначала найдём все staffing записи для этого отдела
        from src.models.staffing import StaffingTable
        stmt = select(StaffingTable.id).where(StaffingTable.department_id == department_id)
        result = await self.db.execute(stmt)
        staffing_ids = [row[0] for row in result.all()]
        if not staffing_ids:
            return []
        # Теперь ищем людей с этими staffing_id
        stmt = select(Person).where(Person.staff_table_id.in_(staffing_ids))
        result = await self.db.execute(stmt)
        return result.scalars().all()