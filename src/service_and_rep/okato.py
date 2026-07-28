from sqlalchemy.ext.asyncio import AsyncSession
from src.models.okato import OKATO
from src.schemas.okato import OKATOResponse
from .base import BaseRepository

class OKATORepository(BaseRepository[OKATO, OKATOResponse, OKATOResponse]):
    def __init__(self, db: AsyncSession):
        super().__init__(OKATO, db)

    # Можно добавить поиск по коду или названию, если нужно