from sqlalchemy import Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import relationship
from src.core.database import Base

class Department(Base):
    __tablename__ = "departments"

    id = Column(Integer, primary_key=True, index=True)
    full_name = Column(String(256), nullable=False)
    short_name = Column(String(256), nullable=False)

    staffing = relationship("StaffingTable", back_populates="department")


class StaffingTable(Base):
    __tablename__ = "staffing_table"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(256))
    count = Column(Integer)
    department_id = Column(Integer, ForeignKey("departments.id"))

    department = relationship("Department", back_populates="staffing")
    persons = relationship("Person", back_populates="staffing")


class Person(Base):
    __tablename__ = "persons"

    id = Column(Integer, primary_key=True, index=True)
    surname = Column(String(256), nullable=False)
    name = Column(String(256), nullable=False)
    middle_name = Column(String(256))
    birth_day = Column(Date, nullable=False)
    sex = Column(String(256))                  # OKIN_01
    citizenship = Column(String(256))          # OKIN_02
    education_level = Column(String(256), nullable=False)  # OKIN_30
    main_profession = Column(String(256))      # OKPDTR_CODE
    other_profession = Column(String(256))     # OKPDTR_CODE
    family_status = Column(String(256))        # OKIN_10
    inn = Column(String(256))
    inn_issue_date = Column(Date)
    snils = Column(String(256))
    snils_issue_date = Column(Date)
    staff_table_id = Column(Integer, ForeignKey("staffing_table.id"))

    staffing = relationship("StaffingTable", back_populates="persons")
    drivers_licenses = relationship("DriversLicense", back_populates="person")
    education_docs = relationship("EducationDoc", back_populates="person")
    languages = relationship("Language", back_populates="person")
    passports = relationship("Passport", back_populates="person")


class DriversLicense(Base):
    __tablename__ = "drivers_licenses"

    id = Column(Integer, primary_key=True, index=True)
    person_id = Column(Integer, ForeignKey("persons.id"))
    series = Column(String(256))
    number = Column(String(256))
    issue_date = Column(Date)
    categories = Column(String(256))

    person = relationship("Person", back_populates="drivers_licenses")


class EducationDoc(Base):
    __tablename__ = "education_docs"

    id = Column(Integer, primary_key=True, index=True)
    person_id = Column(Integer, ForeignKey("persons.id"))
    name = Column(String(256))
    series = Column(String(256))
    number = Column(String(256))
    issue_date = Column(Date)
    organization = Column(String(256))
    okso_code = Column(String(256))

    person = relationship("Person", back_populates="education_docs")


class Language(Base):
    __tablename__ = "languages"

    id = Column(Integer, primary_key=True, index=True)
    person_id = Column(Integer, ForeignKey("persons.id"))
    language = Column(String(256), nullable=False)   # OKIN_04
    knowledge = Column(String(256), nullable=False)  # OKIN_05

    person = relationship("Person", back_populates="languages")


class Passport(Base):
    __tablename__ = "passports"

    id = Column(Integer, primary_key=True, index=True)
    person_id = Column(Integer, ForeignKey("persons.id"))
    series = Column(String(256))
    number = Column(String(256))
    issue_date = Column(Date)
    organization = Column(String(256))
    code = Column(String(256))

    person = relationship("Person", back_populates="passports")