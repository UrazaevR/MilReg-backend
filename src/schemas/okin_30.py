from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class OIN_30Base(BaseModel):
    code: str
    name: str
    autokey: str

class OIN_30Create(OIN_30Base):
    pass

class OIN_30Update(BaseModel):
    code: Optional[str] = None
    name: Optional[str] = None
    autokey: Optional[str] = None

class OIN_30Response(OIN_30Base):
    created_at: datetime
    updated_at: datetime | None = None

    class Config:
        from_attributes = True