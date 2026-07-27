from pydantic import BaseModel, Field
from datetime import datetime
import uuid
from typing import Optional

class StaffingBase(BaseModel):
    name: Optional[str] = Field(None, max_length=256, description="Наименование должности")
    count: Optional[int] = Field(None, description="Количество ставок")
    department_id: Optional[uuid.UUID] = Field(None, description="ID подразделения")

class StaffingCreate(StaffingBase):
    pass

class StaffingUpdate(StaffingBase):
    pass

class StaffingResponse(StaffingBase):
    id: uuid.UUID
    created_at: datetime
    updated_at: datetime | None = None

    class Config:
        from_attributes = True