from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from src.models.drivers_license import DriversLicense
from src.schemas.drivers_license import DriversLicenseCreate, DriversLicenseUpdate
from .base import BaseRepository
import uuid
from typing import Optional, List

class DriversLicenseRepository(BaseRepository[DriversLicense, DriversLicenseCreate, DriversLicenseUpdate]):
    def __init__(self, db: AsyncSession):
        super().__init__(DriversLicense, db)

    async def get_by_person(self, person_id: uuid.UUID) -> List[DriversLicense]:
        """Получить все водительские удостоверения сотрудника."""
        result = await self.db.execute(
            select(DriversLicense).where(DriversLicense.person_id == person_id)
        )
        return result.scalars().all()

    async def get_by_series_number(self, series: str, number: str) -> Optional[DriversLicense]:
        """Найти права по серии и номеру."""
        result = await self.db.execute(
            select(DriversLicense).where(
                DriversLicense.series == series,
                DriversLicense.number == number
            )
        )
        return result.scalar_one_or_none()