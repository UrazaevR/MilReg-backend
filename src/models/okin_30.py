from sqlalchemy import Column, String, DateTime, func
from src.core.database import Base, UUID
import uuid

class OIN_30(Base):
    __tablename__ = "okin_30"

    id = Column(UUID, primary_key=True, default=uuid.uuid4)
    code = Column(String(64), nullable=False, unique=True)
    name = Column(String(255), nullable=False)
    autokey = Column(String(255), nullable=False, unique=True)

    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, onupdate=func.now())