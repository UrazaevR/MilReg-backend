from pydantic import BaseModel
from typing import Optional


class ListMetaBase(BaseModel):
    type: str # list or string

class ListCellMeta(ListMetaBase):
    value: str
    dataEndpoint: Optional[str] = None
    metaEndpoint: Optional[str] = None

class ListListMeta(ListMetaBase):
    value: list[ListCellMeta] | list["ListListMeta"]

class ListMetaResponse(BaseModel):
    list: ListListMeta

    class Config:
        from_attributes = True

