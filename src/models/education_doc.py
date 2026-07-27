from sqlalchemy import Column, String, Date, ForeignKey, DateTime, func
from sqlalchemy.orm import relationship
from src.core.database import Base
from src.core.database import UUID
import uuid

class EducationDoc(Base):
    __tablename__ = "education_docs"

    id = Column(UUID, primary_key=True, default=uuid.uuid4)
    person_id = Column(UUID, ForeignKey("persons.id", ondelete="CASCADE"))
    name = Column(String(256))
    series = Column(String(256))
    number = Column(String(256))
    issue_date = Column(Date)
    organization = Column(String(256))
    okso_code = Column(String(256))
    
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, onupdate=func.now())

    person = relationship("Person", back_populates="education_docs")