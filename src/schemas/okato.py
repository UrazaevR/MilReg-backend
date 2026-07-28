from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class OKATOBase(BaseModel):
    code: str
    name: str
    autokey: str

class OKATOCreate(OKATOBase):
    pass

class OKATOUpdate(BaseModel):
    code: Optional[str] = None
    name: Optional[str] = None
    autokey: Optional[str] = None

class OKATOResponse(OKATOBase):
    created_at: datetime
    updated_at: datetime | None = None

    class Config:
        from_attributes = True