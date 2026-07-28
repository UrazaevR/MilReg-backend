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
    okin_01_router,
    okin_02_router,
    okin_10_router,
    okin_30_router,
    okpdtr_router,
    okato_router,
)
from src.core.database import create_tables, AsyncSessionLocal
from src.core.load_reference_data import load_okato, load_okin, load_okpdtr

@asynccontextmanager
async def lifespan(app: FastAPI):
    create_tables()
    async with AsyncSessionLocal() as session:
        await load_okato(session, "data/ОКАТО.json")
        await load_okin(session, "data/ОКИН.json")        # единый файл
        await load_okpdtr(session, "data/ОКПДТР.json")
    yield

app = FastAPI(
    title="MilReg API",
    version="1.0.0",
    lifespan=lifespan
)

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Подключение роутеров
app.include_router(department_router)
app.include_router(staffing_router)
app.include_router(person_router)
app.include_router(drivers_license_router)
app.include_router(education_doc_router)
app.include_router(language_router)
app.include_router(passport_router)
app.include_router(okin_01_router)
app.include_router(okin_02_router)
app.include_router(okin_10_router)
app.include_router(okin_30_router)
app.include_router(okpdtr_router)
app.include_router(okato_router)

@app.get("/")
async def root():
    return {"message": "MilReg API is running"}