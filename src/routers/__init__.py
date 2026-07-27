from .department import router as department_router
from .staffing import router as staffing_router
from .person import router as person_router
from .drivers_license import router as drivers_license_router
from .education_doc import router as education_doc_router
from .language import router as language_router
from .passport import router as passport_router

__all__ = [
    "department_router",
    "staffing_router",
    "person_router",
    "drivers_license_router",
    "education_doc_router",
    "language_router",
    "passport_router",
]