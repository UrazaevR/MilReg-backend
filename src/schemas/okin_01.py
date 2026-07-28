from pydantic import BaseModel
from datetime import datetime

class OIN_01Base(BaseModel):
    code: str
    name: str
    autokey: str

class OIN_01Response(OIN_01Base):
    created_at: datetime
    updated_at: datetime | None = None

    class Config:
        from_attributes = True