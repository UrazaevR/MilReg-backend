from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from src.models.person import Person
from src.schemas.person import PersonCreate, PersonUpdate
from .base import BaseRepository
import uuid
from typing import Optional, List

class PersonRepository(BaseRepository[Person, PersonCreate, PersonUpdate]):
    def __init__(self, db: AsyncSession):
        super().__init__(Person, db)

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

    async def get_by_department_id(self, department_id: uuid.UUID) -> list[Person]:
        from src.models.staffing import StaffingTable
        stmt = select(StaffingTable.id).where(StaffingTable.department_id == department_id)
        result = await self.db.execute(stmt)
        staffing_ids = [row[0] for row in result.all()]
        if not staffing_ids:
            return []
        stmt = select(Person).where(Person.staff_table_id.in_(staffing_ids))
        result = await self.db.execute(stmt)
        return result.scalars().all()

    async def get_for_list(self):
        persons = await self.get_all()
        answer = []
        for person in persons:
            answer.append(
                {
                    "id": person.id, 
                    "fio": person.surname + ' ' + person.name + (' ' + person.middle_name) if person.middle_name else '',
                    "birth_day": person.birth_day,
                    "main_profession_id": person.main_profession_id,
                    "other_profession_id": person.other_profession_id,
                    "is_training": person.is_training
                }
            )
        return answer