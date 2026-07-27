import uuid
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session
from sqlalchemy import Column, String, func
from sqlalchemy.dialects.postgresql import UUID
from .config import settings

# Функция для генерации UUID
def generate_uuid():
    return str(uuid.uuid4())

# Базовый класс для всех моделей
Base = declarative_base()

# Создаем движок для синхронной работы (для создания таблиц)
engine = create_engine(
    settings.DATABASE_URL.replace("postgresql+asyncpg://", "postgresql://"),
    echo=True
)

# Создаем сессию
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Асинхронная версия для FastAPI
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession

async_engine = create_async_engine(settings.DATABASE_URL, echo=True)
AsyncSessionLocal = async_sessionmaker(async_engine, expire_on_commit=False)

async def get_db() -> AsyncSession:
    async with AsyncSessionLocal() as session:
        yield session

# Функция для создания таблиц
def create_tables():
    """Создает все таблицы в базе данных"""
    Base.metadata.create_all(bind=engine)

# Миксин для добавления UUID поля
class UUIDMixin:
    id = Column(UUID(as_uuid=False), primary_key=True, default=generate_uuid, index=True)