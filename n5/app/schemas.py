from pydantic import BaseModel

class TaskBase(BaseModel):
    title: str
    completed: bool = False

class TaskCreate(TaskBase):
    pass

class TaskUpdate(BaseModel):
    completed: bool

class TaskOut(TaskBase):
    id: int

    class Config:
        orm_mode = True
