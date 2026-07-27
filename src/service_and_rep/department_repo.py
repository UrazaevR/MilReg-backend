from sqlalchemy.ext.asyncio import AsyncSession
from src.core.models import Department
from src.schemas.department import DepartmentCreate, DepartmentUpdate
from .base import BaseRepository

class DepartmentRepository(BaseRepository[Department, DepartmentCreate, DepartmentUpdate]):
    def __init__(self, db: AsyncSession):
        super().__init__(Department, db)

    # Здесь можно добавить дополнительные методы, специфичные для Department
    # Например, поиск по полному имени