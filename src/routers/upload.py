from fastapi import APIRouter, Depends, UploadFile, File, Query, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from src.core.database import get_db
from src.service_and_rep.upload import process_csv_upload

router = APIRouter(prefix="/api/upload", tags=["Upload"])

@router.post("/{entity}")
async def upload_csv(
    entity: str,
    file: UploadFile = File(...),
    mode: str = Query("create", enum=["create", "upsert"]),
    db: AsyncSession = Depends(get_db)
):
    if not file.filename.endswith(".csv"):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Only CSV files are allowed"
        )

    content = await file.read()
    if not content:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Empty file"
        )

    result = await process_csv_upload(db, entity, content, mode)
    return result