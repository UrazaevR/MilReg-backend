from .base import BaseRepository
from .department import DepartmentRepository
from .staffing import StaffingRepository
from .person import PersonRepository
from .drivers_license import DriversLicenseRepository
from .education_doc import EducationDocRepository
from .language import LanguageRepository
from .passport import PassportRepository

__all__ = [
    "BaseRepository",
    "DepartmentRepository",
    "StaffingRepository",
    "PersonRepository",
    "DriversLicenseRepository",
    "EducationDocRepository",
    "LanguageRepository",
    "PassportRepository",
]