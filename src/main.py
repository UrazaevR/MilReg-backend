from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager
from src.routers import (
    department_router,
    staffing_router,
    person_router,
    drivers_license_router,
    education_doc_router,
    language_router,
    passport_router,
)
from src.core.database import create_tables

@asynccontextmanager
async def lifespan(app: FastAPI):
    create_tables()
    yield

app = FastAPI(
    title="HR Management API",
    version="1.0.0",
    lifespan=lifespan
)

# --- Настройка CORS ---
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],                       # Разрешить все источники (для разработки)
    #allow_origins=settings.CORS_ORIGINS or ["*"], # Для прода
    allow_credentials=True,
    allow_methods=["*"],                       # Разрешить все HTTP-методы
    allow_headers=["*"],                       # Разрешить все заголовки
)

# Подключение роутеров
app.include_router(department_router)
app.include_router(staffing_router)
app.include_router(person_router)
app.include_router(drivers_license_router)
app.include_router(education_doc_router)
app.include_router(language_router)
app.include_router(passport_router)

@app.get("/")
async def root():
    return {"message": "HR Management API is running"}