from fastapi import FastAPI
from app.routes.tasks import router as tasks_router
from app.database import create_database

app = FastAPI(
    title="Task Manager",
    description="API для управления задачами",
    version="1.0.0",
)

# Инициализация БД
create_database()

# Роуты
app.include_router(tasks_router)
