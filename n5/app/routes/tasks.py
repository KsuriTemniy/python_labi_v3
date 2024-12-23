from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.schemas import TaskCreate, TaskOut, TaskUpdate
from app.crud import create_task, get_tasks, update_task_status, delete_task
from fastapi.background import BackgroundTasks
from app.email import send_email_stub

router = APIRouter(prefix="/tasks", tags=["Tasks"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=TaskOut)
def create_new_task(task: TaskCreate, background_tasks: BackgroundTasks, db: Session = Depends(get_db)):
    new_task = create_task(db, task)
    background_tasks.add_task(send_email_stub, new_task.title)
    return new_task

@router.get("/", response_model=list[TaskOut])
def read_tasks(completed: bool = Query(None), limit: int = Query(10), db: Session = Depends(get_db)):
    return get_tasks(db, completed, limit)

@router.patch("/{task_id}", response_model=TaskOut)
def update_task(task_id: int, task_update: TaskUpdate, db: Session = Depends(get_db)):
    updated_task = update_task_status(db, task_id, task_update.completed)
    if not updated_task:
        raise HTTPException(status_code=404, detail="Task not found")
    return updated_task

@router.delete("/{task_id}")
def delete_existing_task(task_id: int, db: Session = Depends(get_db)):
    deleted_task = delete_task(db, task_id)
    if not deleted_task:
        raise HTTPException(status_code=404, detail="Task not found")
    return {"detail": "Task deleted"}
