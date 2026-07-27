from pydantic import BaseModel, Field
from datetime import date, datetime
import uuid
from typing import Optional

class DriversLicenseBase(BaseModel):
    person_id: Optional[uuid.UUID] = Field(None, description="ID сотрудника")
    series: Optional[str] = Field(None, max_length=256, description="Серия")
    number: Optional[str] = Field(None, max_length=256, description="Номер")
    issue_date: Optional[date] = Field(None, description="Дата выдачи")
    categories: Optional[str] = Field(None, max_length=256, description="Категории")

class DriversLicenseCreate(DriversLicenseBase):
    pass

class DriversLicenseUpdate(DriversLicenseBase):
    pass

class DriversLicenseResponse(DriversLicenseBase):
    id: uuid.UUID
    created_at: datetime
    updated_at: datetime | None = None

    class Config:
        from_attributes = True