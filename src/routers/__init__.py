from .department import router as department_router
from .staffing import router as staffing_router
from .person import router as person_router
from .drivers_license import router as drivers_license_router
from .education_doc import router as education_doc_router
from .language import router as language_router
from .passport import router as passport_router
from .okato import router as okato_router
from .okin_01 import router as okin_01_router
from .okin_02 import router as okin_02_router
from .okin_10 import router as okin_10_router
from .okin_30 import router as okin_30_router
from .okpdtr import router as okpdtr_router
from .upload import router as upload_router
from .menu import router as menu_router
from .metadata import router as meta_router

__all__ = [
    "department_router",
    "staffing_router",
    "person_router",
    "drivers_license_router",
    "education_doc_router",
    "language_router",
    "passport_router",
    "okato_router",
    "okin_education_router",
    "okin_01_router",
    "okin_02_router",
    "okin_10_router",
    "okin_30_router",
    "okpdtr_router",
    "upload_router",
    "menu_router",
    "meta_router",
]