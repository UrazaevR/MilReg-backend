from pydantic import BaseModel
from datetime import datetime
import uuid

class OKATOBase(BaseModel):
    code: str
    name: str
    autokey: str

class OKATOResponse(OKATOBase):
    id: uuid.UUID
    created_at: datetime
    updated_at: datetime | None = None

    class Config:
        from_attributes = True