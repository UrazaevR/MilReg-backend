from sqlalchemy import Column, String, Integer, ForeignKey, DateTime, func
from sqlalchemy.orm import relationship
from src.core.database import Base
from src.core.database import UUID
import uuid

class StaffingTable(Base):
    __tablename__ = "staffing_table"

    id = Column(UUID, primary_key=True, default=uuid.uuid4)
    name = Column(String(256))
    count = Column(Integer)
    department_id = Column(UUID, ForeignKey("departments.id", ondelete="CASCADE"))
    
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, onupdate=func.now())

    # Связи
    department = relationship("Department", back_populates="staffing")
    persons = relationship("Person", back_populates="staffing", cascade="all, delete-orphan")