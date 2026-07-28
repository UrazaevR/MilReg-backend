from pydantic import BaseModel
from datetime import datetime

class OIN_30Base(BaseModel):
    code: str
    name: str
    autokey: str

class OIN_30Response(OIN_30Base):
    created_at: datetime
    updated_at: datetime | None = None

    class Config:
        from_attributes = True