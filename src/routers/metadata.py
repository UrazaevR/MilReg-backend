from fastapi import APIRouter, HTTPException, status

router = APIRouter(prefix="/api/meta", tags=["metadata"])

@router.get("/{page}")
async def get_meta(page: str):
    raise HTTPException(status_code=status.HTTP_418_IM_A_TEAPOT, detail='Я чайник, остальное в разработке')
    data = {}
    return data