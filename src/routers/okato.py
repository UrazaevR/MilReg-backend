from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from src.core.database import get_db
from src.service_and_rep.okato import OKATORepository
from src.schemas.okato import OKATOResponse
import uuid

router = APIRouter(prefix="/api/okato", tags=["okato"])

@router.get("/", response_model=list[OKATOResponse])
async def get_all_okato(db: AsyncSession = Depends(get_db)):
    repo = OKATORepository(db)
    return await repo.get_all()

@router.get("/{item_id}", response_model=OKATOResponse)
async def get_okato(item_id: uuid.UUID, db: AsyncSession = Depends(get_db)):
    repo = OKATORepository(db)
    item = await repo.get_by_id(item_id)
    if not item:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="OKATO record not found")
    return item