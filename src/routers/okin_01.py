from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from src.core.database import get_db
from src.service_and_rep.okin_01 import OIN_01Repository
from src.schemas.okin_01 import OIN_01Response
import uuid

router = APIRouter(prefix="/api/okin-01", tags=["okin_01"])

@router.get("/", response_model=list[OIN_01Response])
async def get_all(db: AsyncSession = Depends(get_db)):
    repo = OIN_01Repository(db)
    return await repo.get_all()

@router.get("/{item_id}", response_model=OIN_01Response)
async def get_one(item_id: uuid.UUID, db: AsyncSession = Depends(get_db)):
    repo = OIN_01Repository(db)
    item = await repo.get_by_id(item_id)
    if not item:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Not found")
    return item