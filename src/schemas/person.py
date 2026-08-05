from pydantic import BaseModel, Field
from datetime import date, datetime
import uuid
from typing import Optional

class PersonBase(BaseModel):
    surname: str = Field(..., max_length=256)
    name: str = Field(..., max_length=256)
    middle_name: Optional[str] = Field(None, max_length=256)
    birth_day: date
    sex_id: Optional[str] = Field(None, max_length=64)           # код из OKIN_01
    citizenship_id: Optional[str] = Field(None, max_length=64)   # код из OKIN_02
    education_level_id: Optional[str] = Field(None, max_length=64)  # код из OKIN_30
    main_profession_id: Optional[str] = Field(None, max_length=64)  # код из ОКПДТР
    other_profession_id: Optional[str] = Field(None, max_length=64) # код из ОКПДТР
    family_status_id: Optional[str] = Field(None, max_length=64)   # код из OKIN_10
    inn: Optional[str] = Field(None, max_length=256)
    inn_issue_date: Optional[date] = None
    snils: Optional[str] = Field(None, max_length=256)
    snils_issue_date: Optional[date] = None
    is_training: bool = True
    okato_id: Optional[str] = Field(None, max_length=64)         # код из ОКАТО
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

class PersonForListResponse(BaseModel):
    id: uuid.UUID
    fio: str
    birth_day: date
    main_profession_id: Optional[str] = None
    other_profession_id: Optional[str] = None
    is_training: Optional[bool] = True

    class Config:
        from_attributes = True