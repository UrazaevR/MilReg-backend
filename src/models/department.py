from sqlalchemy import Column, String, DateTime, func
from sqlalchemy.orm import relationship
from src.core.database import Base
from src.core.database import UUID
import uuid

class Department(Base):
    __tablename__ = "departments"

    id = Column(UUID, primary_key=True, default=uuid.uuid4)
    full_name = Column(String(256), nullable=False)
    short_name = Column(String(256), nullable=False)
    
    # Аудиторские поля
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, onupdate=func.now())

    # Связи
    staffing = relationship("StaffingTable", back_populates="department", cascade="all, delete-orphan")