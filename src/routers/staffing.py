from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from src.core.database import get_db
from src.service_and_rep.staffing import StaffingRepository
from src.schemas.staffing import StaffingCreate, StaffingUpdate, StaffingResponse
import uuid

router = APIRouter(prefix="/api/staffing", tags=["staffing"])

@router.get("/", response_model=list[StaffingResponse])
async def get_all_staffing(db: AsyncSession = Depends(get_db)):
    repo = StaffingRepository(db)
    return await repo.get_all()

@router.get("/{staff_id}", response_model=StaffingResponse)
async def get_staffing(staff_id: uuid.UUID, db: AsyncSession = Depends(get_db)):
    repo = StaffingRepository(db)
    item = await repo.get_by_id(staff_id)
    if not item:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Staffing record not found")
    return item

@router.post("/", response_model=StaffingResponse, status_code=status.HTTP_201_CREATED)
async def create_staffing(data: StaffingCreate, db: AsyncSession = Depends(get_db)):
    repo = StaffingRepository(db)
    return await repo.create(data)

@router.put("/{staff_id}", response_model=StaffingResponse)
async def update_staffing(staff_id: uuid.UUID, data: StaffingUpdate, db: AsyncSession = Depends(get_db)):
    repo = StaffingRepository(db)
    updated = await repo.update(staff_id, data)
    if not updated:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Staffing record not found")
    return updated

@router.delete("/{staff_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_staffing(staff_id: uuid.UUID, db: AsyncSession = Depends(get_db)):
    repo = StaffingRepository(db)
    deleted = await repo.delete(staff_id)
    if not deleted:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Staffing record not found")
    return