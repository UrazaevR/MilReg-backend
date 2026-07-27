from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from src.core.database import get_db
from src.service_and_rep.language import LanguageRepository
from src.schemas.language import LanguageCreate, LanguageUpdate, LanguageResponse
import uuid

router = APIRouter(prefix="/api/languages", tags=["languages"])

@router.get("/", response_model=list[LanguageResponse])
async def get_all_languages(db: AsyncSession = Depends(get_db)):
    repo = LanguageRepository(db)
    return await repo.get_all()

@router.get("/{lang_id}", response_model=LanguageResponse)
async def get_language(lang_id: uuid.UUID, db: AsyncSession = Depends(get_db)):
    repo = LanguageRepository(db)
    item = await repo.get_by_id(lang_id)
    if not item:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Language record not found")
    return item

@router.post("/", response_model=LanguageResponse, status_code=status.HTTP_201_CREATED)
async def create_language(data: LanguageCreate, db: AsyncSession = Depends(get_db)):
    repo = LanguageRepository(db)
    return await repo.create(data)

@router.put("/{lang_id}", response_model=LanguageResponse)
async def update_language(lang_id: uuid.UUID, data: LanguageUpdate, db: AsyncSession = Depends(get_db)):
    repo = LanguageRepository(db)
    updated = await repo.update(lang_id, data)
    if not updated:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Language record not found")
    return updated

@router.delete("/{lang_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_language(lang_id: uuid.UUID, db: AsyncSession = Depends(get_db)):
    repo = LanguageRepository(db)
    deleted = await repo.delete(lang_id)
    if not deleted:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Language record not found")
    return