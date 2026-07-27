from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from src.core.database import get_db
from src.service_and_rep.education_doc import EducationDocRepository
from src.schemas.education_doc import EducationDocCreate, EducationDocUpdate, EducationDocResponse
import uuid

router = APIRouter(prefix="/api/education-docs", tags=["education_docs"])

@router.get("/", response_model=list[EducationDocResponse])
async def get_all_education_docs(db: AsyncSession = Depends(get_db)):
    repo = EducationDocRepository(db)
    return await repo.get_all()

@router.get("/{doc_id}", response_model=EducationDocResponse)
async def get_education_doc(doc_id: uuid.UUID, db: AsyncSession = Depends(get_db)):
    repo = EducationDocRepository(db)
    item = await repo.get_by_id(doc_id)
    if not item:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Education document not found")
    return item

@router.post("/", response_model=EducationDocResponse, status_code=status.HTTP_201_CREATED)
async def create_education_doc(data: EducationDocCreate, db: AsyncSession = Depends(get_db)):
    repo = EducationDocRepository(db)
    return await repo.create(data)

@router.put("/{doc_id}", response_model=EducationDocResponse)
async def update_education_doc(doc_id: uuid.UUID, data: EducationDocUpdate, db: AsyncSession = Depends(get_db)):
    repo = EducationDocRepository(db)
    updated = await repo.update(doc_id, data)
    if not updated:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Education document not found")
    return updated

@router.delete("/{doc_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_education_doc(doc_id: uuid.UUID, db: AsyncSession = Depends(get_db)):
    repo = EducationDocRepository(db)
    deleted = await repo.delete(doc_id)
    if not deleted:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Education document not found")
    return