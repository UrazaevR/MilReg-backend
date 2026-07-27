from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from src.models.language import Language
from src.schemas.language import LanguageCreate, LanguageUpdate
from .base import BaseRepository
import uuid
from typing import Optional, List

class LanguageRepository(BaseRepository[Language, LanguageCreate, LanguageUpdate]):
    def __init__(self, db: AsyncSession):
        super().__init__(Language, db)

    async def get_by_person(self, person_id: uuid.UUID) -> List[Language]:
        """Получить все языки сотрудника."""
        result = await self.db.execute(
            select(Language).where(Language.person_id == person_id)
        )
        return result.scalars().all()

    async def get_by_language_and_knowledge(self, language: str, knowledge: str) -> List[Language]:
        """Найти записи по языку и уровню знания."""
        result = await self.db.execute(
            select(Language).where(
                Language.language == language,
                Language.knowledge == knowledge
            )
        )
        return result.scalars().all()