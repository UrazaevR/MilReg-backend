from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from src.core.database import get_db
from src.service_and_rep.drivers_license import DriversLicenseRepository
from src.schemas.drivers_license import DriversLicenseCreate, DriversLicenseUpdate, DriversLicenseResponse
import uuid

router = APIRouter(prefix="/api/drivers-licenses", tags=["drivers_licenses"])

@router.get("/", response_model=list[DriversLicenseResponse])
async def get_all_licenses(db: AsyncSession = Depends(get_db)):
    repo = DriversLicenseRepository(db)
    return await repo.get_all()

@router.get("/{license_id}", response_model=DriversLicenseResponse)
async def get_license(license_id: uuid.UUID, db: AsyncSession = Depends(get_db)):
    repo = DriversLicenseRepository(db)
    item = await repo.get_by_id(license_id)
    if not item:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Driver's license not found")
    return item

@router.post("/", response_model=DriversLicenseResponse, status_code=status.HTTP_201_CREATED)
async def create_license(data: DriversLicenseCreate, db: AsyncSession = Depends(get_db)):
    repo = DriversLicenseRepository(db)
    return await repo.create(data)

@router.put("/{license_id}", response_model=DriversLicenseResponse)
async def update_license(license_id: uuid.UUID, data: DriversLicenseUpdate, db: AsyncSession = Depends(get_db)):
    repo = DriversLicenseRepository(db)
    updated = await repo.update(license_id, data)
    if not updated:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Driver's license not found")
    return updated

@router.delete("/{license_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_license(license_id: uuid.UUID, db: AsyncSession = Depends(get_db)):
    repo = DriversLicenseRepository(db)
    deleted = await repo.delete(license_id)
    if not deleted:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Driver's license not found")
    return