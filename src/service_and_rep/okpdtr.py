from sqlalchemy.ext.asyncio import AsyncSession
from src.models.okpdtr import OKPDTR
from src.schemas.okpdtr import OKPDTRResponse
from src.service_and_rep.base import BaseRepository

class OKPDTRRepository(BaseRepository[OKPDTR, OKPDTRResponse, OKPDTRResponse]):
    def __init__(self, db: AsyncSession):
        super().__init__(OKPDTR, db)