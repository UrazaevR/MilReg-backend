from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from src.core.database import get_db
from src.service_and_rep.department import DepartmentRepository
from src.schemas.department import DepartmentCreate, DepartmentUpdate, DepartmentResponse
import uuid

router = APIRouter(prefix="/api/departments", tags=["departments"])

@router.get("/", response_model=list[DepartmentResponse])
async def get_all_departments(db: AsyncSession = Depends(get_db)):
    repo = DepartmentRepository(db)
    return await repo.get_all()

@router.get("/{dept_id}", response_model=DepartmentResponse)
async def get_department(dept_id: uuid.UUID, db: AsyncSession = Depends(get_db)):
    repo = DepartmentRepository(db)
    dept = await repo.get_by_id(dept_id)
    if not dept:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Department not found")
    return dept

@router.post("/", response_model=DepartmentResponse, status_code=status.HTTP_201_CREATED)
async def create_department(data: DepartmentCreate, db: AsyncSession = Depends(get_db)):
    repo = DepartmentRepository(db)
    return await repo.create(data)

@router.put("/{dept_id}", response_model=DepartmentResponse)
async def update_department(dept_id: uuid.UUID, data: DepartmentUpdate, db: AsyncSession = Depends(get_db)):
    repo = DepartmentRepository(db)
    updated = await repo.update(dept_id, data)
    if not updated:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Department not found")
    return updated

@router.delete("/{dept_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_department(dept_id: uuid.UUID, db: AsyncSession = Depends(get_db)):
    repo = DepartmentRepository(db)
    deleted = await repo.delete(dept_id)
    if not deleted:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Department not found")
    return