from sqlalchemy.ext.asyncio import AsyncSession
from src.models.okin_30 import OIN_30
from src.schemas.okin_30 import OIN_30Response
from .base import BaseRepository

class OIN_30Repository(BaseRepository[OIN_30, OIN_30Response, OIN_30Response]):
    def __init__(self, db: AsyncSession):
        super().__init__(OIN_30, db)