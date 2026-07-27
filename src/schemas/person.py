from pydantic import BaseModel, Field
from datetime import date, datetime
import uuid
from typing import Optional

class PersonBase(BaseModel):
    surname: str = Field(..., max_length=256, description="Фамилия")
    name: str = Field(..., max_length=256, description="Имя")
    middle_name: Optional[str] = Field(None, max_length=256, description="Отчество")
    birth_day: date = Field(..., description="Дата рождения")
    sex: Optional[str] = Field(None, max_length=256, description="Пол (OKIN_01)")
    citizenship: Optional[str] = Field(None, max_length=256, description="Гражданство (OKIN_02)")
    education_level: str = Field(..., max_length=256, description="Уровень образования (OKIN_30)")
    main_profession: Optional[str] = Field(None, max_length=256, description="Основная профессия (OKPDTR)")
    other_profession: Optional[str] = Field(None, max_length=256, description="Другая профессия (OKPDTR)")
    family_status: Optional[str] = Field(None, max_length=256, description="Семейное положение (OKIN_10)")
    inn: Optional[str] = Field(None, max_length=256, description="ИНН")
    inn_issue_date: Optional[date] = Field(None, description="Дата выдачи ИНН")
    snils: Optional[str] = Field(None, max_length=256, description="СНИЛС")
    snils_issue_date: Optional[date] = Field(None, description="Дата выдачи СНИЛС")
    is_training: bool = Field(True, description="Статус обучения (по умолчанию True)")
    staff_table_id: Optional[uuid.UUID] = Field(None, description="ID штатной единицы")

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