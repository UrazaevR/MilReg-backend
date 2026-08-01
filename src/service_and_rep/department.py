from typing import Optional
from sqlalchemy.ext.asyncio import AsyncSession
from src.models.department import Department
from src.schemas.department import DepartmentCreate, DepartmentUpdate
from .base import BaseRepository

class DepartmentRepository(BaseRepository[Department, DepartmentCreate, DepartmentUpdate]):
    def __init__(self, db: AsyncSession):
        super().__init__(Department, db)

    # Дополнительные методы, если нужны
    # например, поиск по полному имени
    async def get_by_full_name(self, full_name: str) -> Optional[Department]:
        from sqlalchemy import select
        result = await self.db.execute(
            select(Department).where(Department.full_name == full_name)
        )
        return result.scalar_one_or_none()