from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from src.core.database import get_db
from src.service_and_rep.passport import PassportRepository
from src.schemas.passport import PassportCreate, PassportUpdate, PassportResponse
import uuid

router = APIRouter(prefix="/api/passports", tags=["passports"])

@router.get("/", response_model=list[PassportResponse])
async def get_all_passports(db: AsyncSession = Depends(get_db)):
    repo = PassportRepository(db)
    return await repo.get_all()

@router.get("/{passport_id}", response_model=PassportResponse)
async def get_passport(passport_id: uuid.UUID, db: AsyncSession = Depends(get_db)):
    repo = PassportRepository(db)
    item = await repo.get_by_id(passport_id)
    if not item:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Passport not found")
    return item

@router.post("/", response_model=PassportResponse, status_code=status.HTTP_201_CREATED)
async def create_passport(data: PassportCreate, db: AsyncSession = Depends(get_db)):
    repo = PassportRepository(db)
    return await repo.create(data)

@router.put("/{passport_id}", response_model=PassportResponse)
async def update_passport(passport_id: uuid.UUID, data: PassportUpdate, db: AsyncSession = Depends(get_db)):
    repo = PassportRepository(db)
    updated = await repo.update(passport_id, data)
    if not updated:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Passport not found")
    return updated

@router.delete("/{passport_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_passport(passport_id: uuid.UUID, db: AsyncSession = Depends(get_db)):
    repo = PassportRepository(db)
    deleted = await repo.delete(passport_id)
    if not deleted:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Passport not found")
    return