from sqlalchemy import Column, String, DateTime, func
from src.core.database import Base

class OIN_10(Base):
    __tablename__ = "okin_10"

    code = Column(String(64), primary_key=True, nullable=False)
    name = Column(String(255), nullable=False)
    autokey = Column(String(255), nullable=False, unique=True)

    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, onupdate=func.now())