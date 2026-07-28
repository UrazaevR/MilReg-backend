from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class OKPDTRBase(BaseModel):
    code: str
    kch: Optional[str] = None
    profession_name: Optional[str] = None
    job_name: Optional[str] = None
    code_category: Optional[str] = None
    code_etks: Optional[str] = None
    code_okz: Optional[str] = None
    autokey: str

class OKPDTRResponse(OKPDTRBase):
    created_at: datetime
    updated_at: datetime | None = None

    class Config:
        from_attributes = True