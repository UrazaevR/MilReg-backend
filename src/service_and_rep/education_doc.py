from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from src.models.education_doc import EducationDoc
from src.schemas.education_doc import EducationDocCreate, EducationDocUpdate
from .base import BaseRepository
import uuid
from typing import Optional, List

class EducationDocRepository(BaseRepository[EducationDoc, EducationDocCreate, EducationDocUpdate]):
    def __init__(self, db: AsyncSession):
        super().__init__(EducationDoc, db)

    async def get_by_person(self, person_id: uuid.UUID) -> List[EducationDoc]:
        """Получить все документы об образовании сотрудника."""
        result = await self.db.execute(
            select(EducationDoc).where(EducationDoc.person_id == person_id)
        )
        return result.scalars().all()

    async def get_by_series_number(self, series: str, number: str) -> Optional[EducationDoc]:
        """Найти документ по серии и номеру."""
        result = await self.db.execute(
            select(EducationDoc).where(
                EducationDoc.series == series,
                EducationDoc.number == number
            )
        )
        return result.scalar_one_or_none()