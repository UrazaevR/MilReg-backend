from pydantic import BaseModel
from datetime import datetime

class OIN_10Base(BaseModel):
    code: str
    name: str
    autokey: str

class OIN_10Response(OIN_10Base):
    created_at: datetime
    updated_at: datetime | None = None

    class Config:
        from_attributes = True