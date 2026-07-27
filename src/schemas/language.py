from pydantic import BaseModel, Field
from datetime import datetime
import uuid
from typing import Optional

class LanguageBase(BaseModel):
    person_id: Optional[uuid.UUID] = Field(None, description="ID сотрудника")
    language: str = Field(..., max_length=256, description="Язык (OKIN_04)")
    knowledge: str = Field(..., max_length=256, description="Степень знания (OKIN_05)")

class LanguageCreate(LanguageBase):
    pass

class LanguageUpdate(LanguageBase):
    pass

class LanguageResponse(LanguageBase):
    id: uuid.UUID
    created_at: datetime
    updated_at: datetime | None = None

    class Config:
        from_attributes = True