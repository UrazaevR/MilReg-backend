from sqlalchemy import Column, String, DateTime, func
from sqlalchemy.orm import relationship
from src.core.database import Base, UUID
import uuid

class OKATO(Base):
    __tablename__ = "okato"

    id = Column(UUID, primary_key=True, default=uuid.uuid4)
    code = Column(String(255), nullable=False, unique=True)   # код ОКАТО
    name = Column(String(255), nullable=False)                # название региона
    autokey = Column(String(255), nullable=False, unique=True)

    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, onupdate=func.now())

    persons = relationship("Person", back_populates="okato")