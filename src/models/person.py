from sqlalchemy import Column, String, Date, ForeignKey, Boolean, DateTime, func
from sqlalchemy.orm import relationship
from src.core.database import Base
from src.core.database import UUID
import uuid

class Person(Base):
    __tablename__ = "persons"

    id = Column(UUID, primary_key=True, default=uuid.uuid4)
    surname = Column(String(256), nullable=False)
    name = Column(String(256), nullable=False)
    middle_name = Column(String(256))
    birth_day = Column(Date, nullable=False)
    sex = Column(String(256))  # OKIN_01
    citizenship = Column(String(256))  # OKIN_02
    education_level = Column(String(256), nullable=False)  # OKIN_30
    main_profession = Column(String(256))  # OKPDTR_CODE
    other_profession = Column(String(256))  # OKPDTR_CODE
    family_status = Column(String(256))  # OKIN_10
    inn = Column(String(256))
    inn_issue_date = Column(Date)
    snils = Column(String(256))
    snils_issue_date = Column(Date)
    is_training = Column(Boolean, default=True)  # Новое поле
    staff_table_id = Column(UUID, ForeignKey("staffing_table.id", ondelete="SET NULL"))
    
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, onupdate=func.now())

    # Связи
    staffing = relationship("StaffingTable", back_populates="persons")
    drivers_licenses = relationship("DriversLicense", back_populates="person", cascade="all, delete-orphan")
    education_docs = relationship("EducationDoc", back_populates="person", cascade="all, delete-orphan")
    languages = relationship("Language", back_populates="person", cascade="all, delete-orphan")
    passports = relationship("Passport", back_populates="person", cascade="all, delete-orphan")