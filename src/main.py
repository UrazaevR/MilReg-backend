from fastapi import FastAPI
from src.routers import departments

app = FastAPI(title="My Project API", version="0.1.0")

# Подключаем роутеры
app.include_router(departments.router, prefix="/api")

@app.get("/")
async def root():
    return {"message": "Welcome to the API"}