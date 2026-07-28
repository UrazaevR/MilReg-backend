from sqlalchemy.ext.asyncio import AsyncSession
from src.models.okin_10 import OIN_10
from src.schemas.okin_10 import OIN_10Response
from .base import BaseRepository

class OIN_10Repository(BaseRepository[OIN_10, OIN_10Response, OIN_10Response]):
    def __init__(self, db: AsyncSession):
        super().__init__(OIN_10, db)