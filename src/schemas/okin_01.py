from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class OIN_01Base(BaseModel):
    code: str
    name: str
    autokey: str

class OIN_01Create(OIN_01Base):
    pass

class OIN_01Update(BaseModel):
    code: Optional[str] = None
    name: Optional[str] = None
    autokey: Optional[str] = None

class OIN_01Response(OIN_01Base):
    created_at: datetime
    updated_at: datetime | None = None

    class Config:
        from_attributes = True