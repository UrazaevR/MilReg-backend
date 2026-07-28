from sqlalchemy import Column, String, Date, ForeignKey, Boolean, DateTime, func
from sqlalchemy.orm import relationship
from src.core.database import Base, UUID
import uuid

class Person(Base):
    __tablename__ = "persons"

    id = Column(UUID, primary_key=True, default=uuid.uuid4)
    surname = Column(String(256), nullable=False)
    name = Column(String(256), nullable=False)
    middle_name = Column(String(256))
    birth_day = Column(Date, nullable=False)

    # Внешние ключи на справочники (теперь строковые)
    sex_id = Column(String(64), ForeignKey("okin_01.code", ondelete="SET NULL"), nullable=True)
    citizenship_id = Column(String(64), ForeignKey("okin_02.code", ondelete="SET NULL"), nullable=True)
    education_level_id = Column(String(64), ForeignKey("okin_30.code", ondelete="SET NULL"), nullable=True)
    main_profession_id = Column(String(64), ForeignKey("okpdtr.code", ondelete="SET NULL"), nullable=True)
    other_profession_id = Column(String(64), ForeignKey("okpdtr.code", ondelete="SET NULL"), nullable=True)
    family_status_id = Column(String(64), ForeignKey("okin_10.code", ondelete="SET NULL"), nullable=True)
    okato_id = Column(String(64), ForeignKey("okato.code", ondelete="SET NULL"), nullable=True)

    inn = Column(String(256))
    inn_issue_date = Column(Date)
    snils = Column(String(256))
    snils_issue_date = Column(Date)
    is_training = Column(Boolean, default=True)
    staff_table_id = Column(UUID, ForeignKey("staffing_table.id", ondelete="SET NULL"))

    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, onupdate=func.now())

    # Связи
    okato = relationship("OKATO", back_populates="persons")
    staffing = relationship("StaffingTable", back_populates="persons")
    sex = relationship("OIN_01")
    citizenship = relationship("OIN_02")
    family_status = relationship("OIN_10")
    education_level = relationship("OIN_30")
    main_profession = relationship("OKPDTR", foreign_keys=[main_profession_id])
    other_profession = relationship("OKPDTR", foreign_keys=[other_profession_id])

    drivers_licenses = relationship("DriversLicense", back_populates="person", cascade="all, delete-orphan")
    education_docs = relationship("EducationDoc", back_populates="person", cascade="all, delete-orphan")
    languages = relationship("Language", back_populates="person", cascade="all, delete-orphan")
    passports = relationship("Passport", back_populates="person", cascade="all, delete-orphan")