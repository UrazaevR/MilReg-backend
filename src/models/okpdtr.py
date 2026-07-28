from sqlalchemy import Column, String, DateTime, func
from sqlalchemy.orm import relationship
from src.core.database import Base, UUID
import uuid

class OKPDTR(Base):
    __tablename__ = "okpdtr"

    id = Column(UUID, primary_key=True, default=uuid.uuid4)
    code = Column(String(64), nullable=False, unique=True)       # код профессии
    kch = Column(String(4), nullable=True)                       # КЧ
    profession_name = Column(String(256), nullable=True)         # наименование профессии
    job_name = Column(String(256), nullable=True)                # наименование должности
    code_category = Column(String(64), nullable=True)            # код категории
    code_etks = Column(String(64), nullable=True)                # код выпуска ЕТКС
    code_okz = Column(String(64), nullable=True)                 # код по ОКЗ
    autokey = Column(String(255), nullable=False, unique=True)   # ключ

    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, onupdate=func.now())

    # Связи с Person (обратные)
    persons_main = relationship("Person", foreign_keys="Person.main_profession_id", back_populates="main_profession")
    persons_other = relationship("Person", foreign_keys="Person.other_profession_id", back_populates="other_profession")