from sqlalchemy.ext.asyncio import AsyncSession
from src.models.okin_02 import OIN_02
from src.schemas.okin_02 import OIN_02Response
from .base import BaseRepository

class OIN_02Repository(BaseRepository[OIN_02, OIN_02Response, OIN_02Response]):
    def __init__(self, db: AsyncSession):
        super().__init__(OIN_02, db)