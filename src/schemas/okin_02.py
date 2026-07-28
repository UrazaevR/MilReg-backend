from pydantic import BaseModel
from datetime import datetime
import uuid

class OIN_02Base(BaseModel):
    code: str
    name: str
    autokey: str

class OIN_02Response(OIN_02Base):
    id: uuid.UUID
    created_at: datetime
    updated_at: datetime | None = None

    class Config:
        from_attributes = True