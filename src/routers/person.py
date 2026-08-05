from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from src.core.database import get_db
from src.service_and_rep.person import PersonRepository
from src.schemas.person import PersonCreate, PersonUpdate, PersonResponse, PersonForListResponse
import uuid

router = APIRouter(prefix="/api/persons", tags=["persons"])

@router.get("/", response_model=list[PersonResponse])
async def get_all_persons(db: AsyncSession = Depends(get_db)):
    repo = PersonRepository(db)
    return await repo.get_all()

@router.get("/list", response_model=list[PersonForListResponse])
async def get_list_of_persons(db: AsyncSession = Depends(get_db)):
    repo = PersonRepository(db)
    return await repo.get_for_list()

@router.get("/{person_id}", response_model=PersonResponse)
async def get_person(person_id: uuid.UUID, db: AsyncSession = Depends(get_db)):
    repo = PersonRepository(db)
    person = await repo.get_by_id(person_id)
    if not person:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Person not found")
    return person

@router.post("/", response_model=PersonResponse, status_code=status.HTTP_201_CREATED)
async def create_person(data: PersonCreate, db: AsyncSession = Depends(get_db)):
    repo = PersonRepository(db)
    return await repo.create(data)

@router.put("/{person_id}", response_model=PersonResponse)
async def update_person(person_id: uuid.UUID, data: PersonUpdate, db: AsyncSession = Depends(get_db)):
    repo = PersonRepository(db)
    updated = await repo.update(person_id, data)
    if not updated:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Person not found")
    return updated

@router.delete("/{person_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_person(person_id: uuid.UUID, db: AsyncSession = Depends(get_db)):
    repo = PersonRepository(db)
    deleted = await repo.delete(person_id)
    if not deleted:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Person not found")
    return