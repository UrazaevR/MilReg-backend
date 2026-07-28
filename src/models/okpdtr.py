from sqlalchemy import Column, String, DateTime, func
from sqlalchemy.orm import relationship
from src.core.database import Base

class OKPDTR(Base):
    __tablename__ = "okpdtr"

    code = Column(String(64), primary_key=True, nullable=False)   # код профессии
    kch = Column(String(4), nullable=True)
    profession_name = Column(String(256), nullable=True)
    job_name = Column(String(256), nullable=True)
    code_category = Column(String(64), nullable=True)
    code_etks = Column(String(64), nullable=True)
    code_okz = Column(String(64), nullable=True)
    autokey = Column(String(255), nullable=False, unique=True)

    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, onupdate=func.now())

    persons_main = relationship("Person", foreign_keys="Person.main_profession_id", back_populates="main_profession")
    persons_other = relationship("Person", foreign_keys="Person.other_profession_id", back_populates="other_profession")