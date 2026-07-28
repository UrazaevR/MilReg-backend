from pydantic import BaseModel
from datetime import datetime
import uuid

class OIN_10Base(BaseModel):
    code: str
    name: str
    autokey: str

class OIN_10Response(OIN_10Base):
    id: uuid.UUID
    created_at: datetime
    updated_at: datetime | None = None

    class Config:
        from_attributes = True