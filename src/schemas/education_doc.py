from pydantic import BaseModel, Field
from datetime import date, datetime
import uuid
from typing import Optional

class EducationDocBase(BaseModel):
    person_id: Optional[uuid.UUID] = Field(None, description="ID сотрудника")
    name: Optional[str] = Field(None, max_length=256, description="Наименование документа")
    series: Optional[str] = Field(None, max_length=256, description="Серия")
    number: Optional[str] = Field(None, max_length=256, description="Номер")
    issue_date: Optional[date] = Field(None, description="Дата выдачи")
    organization: Optional[str] = Field(None, max_length=256, description="Организация")
    okso_code: Optional[str] = Field(None, max_length=256, description="Код ОКСО")

class EducationDocCreate(EducationDocBase):
    pass

class EducationDocUpdate(EducationDocBase):
    pass

class EducationDocResponse(EducationDocBase):
    id: uuid.UUID
    created_at: datetime
    updated_at: datetime | None = None

    class Config:
        from_attributes = True