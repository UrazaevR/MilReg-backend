from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class OIN_10Base(BaseModel):
    code: str
    name: str
    autokey: str

class OIN_10Create(OIN_10Base):
    pass

class OIN_10Update(BaseModel):
    code: Optional[str] = None
    name: Optional[str] = None
    autokey: Optional[str] = None

class OIN_10Response(OIN_10Base):
    created_at: datetime
    updated_at: datetime | None = None

    class Config:
        from_attributes = True