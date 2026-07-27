from pydantic import BaseModel, Field
from datetime import datetime
import uuid

class DepartmentBase(BaseModel):
    full_name: str = Field(..., max_length=256, description="Полное наименование")
    short_name: str = Field(..., max_length=256, description="Краткое наименование")

class DepartmentCreate(DepartmentBase):
    pass

class DepartmentUpdate(DepartmentBase):
    pass

class DepartmentResponse(DepartmentBase):
    id: uuid.UUID
    created_at: datetime
    updated_at: datetime | None = None

    class Config:
        from_attributes = True