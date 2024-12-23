from fastapi import FastAPI
from routes.tasks import router as tasks_router
from database import create_database

app = FastAPI(
    title="Task Manager",
    description="API для управления задачами",
    version="1.0.0",
)

# Инициализация БД
create_database()
@app.get("/")
def read_root():
    return {"message": "Welcome to the Task Manager API. Visit /docs for Swagger UI."}

# Роуты
app.include_router(tasks_router)
