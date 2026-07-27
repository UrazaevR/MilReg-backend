from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from src.models.passport import Passport
from src.schemas.passport import PassportCreate, PassportUpdate
from .base import BaseRepository
import uuid
from typing import Optional, List

class PassportRepository(BaseRepository[Passport, PassportCreate, PassportUpdate]):
    def __init__(self, db: AsyncSession):
        super().__init__(Passport, db)

    async def get_by_person(self, person_id: uuid.UUID) -> List[Passport]:
        """Получить все паспорта сотрудника."""
        result = await self.db.execute(
            select(Passport).where(Passport.person_id == person_id)
        )
        return result.scalars().all()

    async def get_by_series_number(self, series: str, number: str) -> Optional[Passport]:
        """Найти паспорт по серии и номеру."""
        result = await self.db.execute(
            select(Passport).where(
                Passport.series == series,
                Passport.number == number
            )
        )
        return result.scalar_one_or_none()