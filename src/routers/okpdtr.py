from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from src.core.database import get_db
from src.service_and_rep.okpdtr import OKPDTRRepository
from src.schemas.okpdtr import OKPDTRResponse
import uuid

router = APIRouter(prefix="/api/okpdtr", tags=["okpdtr"])

@router.get("/", response_model=list[OKPDTRResponse])
async def get_all(db: AsyncSession = Depends(get_db)):
    repo = OKPDTRRepository(db)
    return await repo.get_all()

@router.get("/{item_id}", response_model=OKPDTRResponse)
async def get_one(item_id: uuid.UUID, db: AsyncSession = Depends(get_db)):
    repo = OKPDTRRepository(db)
    item = await repo.get_by_id(item_id)
    if not item:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Not found")
    return item