from sqlalchemy import Column, String, DateTime, func
from sqlalchemy.orm import relationship
from src.core.database import Base

class OKATO(Base):
    __tablename__ = "okato"

    code = Column(String(255), primary_key=True, nullable=False)   # код ОКАТО
    name = Column(String(255), nullable=False)                    # название региона
    autokey = Column(String(255), nullable=False, unique=True)

    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, onupdate=func.now())

    persons = relationship("Person", back_populates="okato")