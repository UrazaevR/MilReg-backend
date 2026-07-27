from pydantic import BaseModel, Field
from datetime import date, datetime
import uuid
from typing import Optional

class PassportBase(BaseModel):
    person_id: Optional[uuid.UUID] = Field(None, description="ID сотрудника")
    series: Optional[str] = Field(None, max_length=256, description="Серия")
    number: Optional[str] = Field(None, max_length=256, description="Номер")
    issue_date: Optional[date] = Field(None, description="Дата выдачи")
    organization: Optional[str] = Field(None, max_length=256, description="Кем выдан")
    code: Optional[str] = Field(None, max_length=256, description="Код подразделения")

class PassportCreate(PassportBase):
    pass

class PassportUpdate(PassportBase):
    pass

class PassportResponse(PassportBase):
    id: uuid.UUID
    created_at: datetime
    updated_at: datetime | None = None

    class Config:
        from_attributes = True