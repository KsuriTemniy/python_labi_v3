from sqlalchemy.orm import Session
from app.models import Task
from app.schemas import TaskCreate
def create_task(db: Session, task: TaskCreate):
    db_task = Task(title=task.title)
    db.add(db_task)
    db.commit()
    db.refresh(db_task)
    return db_task

def get_tasks(db: Session, completed: bool = None, limit: int = 10):
    query = db.query(Task)
    if completed is not None:
        query = query.filter(Task.completed == completed)
    return query.limit(limit).all()

def update_task_status(db: Session, task_id: int, completed: bool):
    task = db.query(Task).filter(Task.id == task_id).first()
    if task:
        task.completed = completed
        db.commit()
        return task
    return None

def delete_task(db: Session, task_id: int):
    task = db.query(Task).filter(Task.id == task_id).first()
    if task:
        db.delete(task)
        db.commit()
        return task
    return None
