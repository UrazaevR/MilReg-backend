from fastapi import APIRouter, HTTPException, status
from src.schemas import ListCellMeta, ListListMeta, ListMetaResponse

router = APIRouter(prefix="/api/meta", tags=["metadata"])

@router.get("/{page}")
async def get_meta(page: str):
    match page:
        case "persons":
            data = ListListMeta(type='list',
                value=[
                    ListCellMeta(type='string', value='id'),
                    ListListMeta(type='list', value=[
                        ListCellMeta(type='string', value='fio', dataEndpoint='api/persons/{id}'),
                        ListCellMeta(type='date', value='birth_day')
                    ]),
                    ListListMeta(type='list', value=[
                        ListCellMeta(type='string', value='main_profession_id'),
                        ListCellMeta(type='string', value='other_profession_id')
                    ]),
                    ListCellMeta(type='boolean', value='is_training')
                ]
            )
            return data
        case _:
            raise HTTPException(status_code=status.HTTP_418_IM_A_TEAPOT, detail='Я чайник, остальное в разработке')
    

    