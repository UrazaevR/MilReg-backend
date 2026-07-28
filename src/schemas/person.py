from pydantic import BaseModel, Field
from datetime import date, datetime
import uuid
from typing import Optional

class PersonBase(BaseModel):
    surname: str = Field(..., max_length=256)
    name: str = Field(..., max_length=256)
    middle_name: Optional[str] = Field(None, max_length=256)
    birth_day: date
    sex_id: Optional[uuid.UUID] = None                     # OKIN_01
    citizenship_id: Optional[uuid.UUID] = None             # OKIN_02
    education_level_id: Optional[uuid.UUID] = None         # OKIN_30 (вместо строки)
    main_profession_id: Optional[uuid.UUID] = None         # ОКПДТР
    other_profession_id: Optional[uuid.UUID] = None        # ОКПДТР
    family_status_id: Optional[uuid.UUID] = None           # OKIN_10
    inn: Optional[str] = Field(None, max_length=256)
    inn_issue_date: Optional[date] = None
    snils: Optional[str] = Field(None, max_length=256)
    snils_issue_date: Optional[date] = None
    is_training: bool = True
    okato_id: Optional[uuid.UUID] = None                   # ОКАТО (было region_id)
    staff_table_id: Optional[uuid.UUID] = None

class PersonCreate(PersonBase):
    pass

class PersonUpdate(PersonBase):
    pass

class PersonResponse(PersonBase):
    id: uuid.UUID
    created_at: datetime
    updated_at: datetime | None = None

    class Config:
        from_attributes = True