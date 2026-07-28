from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from src.core.database import get_db
from src.service_and_rep.okin_02 import OIN_02Repository
from src.schemas.okin_02 import OIN_02Response
import uuid

router = APIRouter(prefix="/api/okin-02", tags=["okin_02"])

@router.get("/", response_model=list[OIN_02Response])
async def get_all(db: AsyncSession = Depends(get_db)):
    repo = OIN_02Repository(db)
    return await repo.get_all()

@router.get("/{item_id}", response_model=OIN_02Response)
async def get_one(item_id: uuid.UUID, db: AsyncSession = Depends(get_db)):
    repo = OIN_02Repository(db)
    item = await repo.get_by_id(item_id)
    if not item:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Not found")
    return item