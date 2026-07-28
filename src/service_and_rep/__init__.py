from .base import BaseRepository
from .department import DepartmentRepository
from .staffing import StaffingRepository
from .person import PersonRepository
from .drivers_license import DriversLicenseRepository
from .education_doc import EducationDocRepository
from .language import LanguageRepository
from .passport import PassportRepository
from .okato import OKATORepository
from .okin_01 import OIN_01Repository
from .okin_02 import OIN_02Repository
from .okin_10 import OIN_10Repository
from .okpdtr import OKPDTRRepository

__all__ = [
    "BaseRepository",
    "DepartmentRepository",
    "StaffingRepository",
    "PersonRepository",
    "DriversLicenseRepository",
    "EducationDocRepository",
    "LanguageRepository",
    "PassportRepository",
    "OKATORepository",
    "OKINEducationRepository",
    "OIN_01Repository",
    "OIN_02Repository",
    "OIN_10Repository",
    "OKPDTRRepository",
]