from sqlalchemy.ext.asyncio import AsyncSession
from src.models.okin_01 import OIN_01
from src.schemas.okin_01 import OIN_01Response
from .base import BaseRepository

class OIN_01Repository(BaseRepository[OIN_01, OIN_01Response, OIN_01Response]):
    def __init__(self, db: AsyncSession):
        super().__init__(OIN_01, db)