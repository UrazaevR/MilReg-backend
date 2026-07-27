from sqlalchemy import Column, String, ForeignKey, DateTime, func
from sqlalchemy.orm import relationship
from src.core.database import Base
from src.core.database import UUID
import uuid

class Language(Base):
    __tablename__ = "languages"

    id = Column(UUID, primary_key=True, default=uuid.uuid4)
    person_id = Column(UUID, ForeignKey("persons.id", ondelete="CASCADE"))
    language = Column(String(256), nullable=False)  # OKIN_04
    knowledge = Column(String(256), nullable=False)  # OKIN_05
    
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, onupdate=func.now())

    person = relationship("Person", back_populates="languages")