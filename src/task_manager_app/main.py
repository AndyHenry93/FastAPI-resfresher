from typing import List
from typing import Optional

from fastapi import Depends
from fastapi import FastAPI
from fastapi import HTTPException
from sqlalchemy.orm import Session

from .database import SessionLocal
from .database import Tasks
from .models import Task
from .models import TaskResponse
from .models import TaskV2
from .models import TaskV2Response
from .operations import create_task
from .operations import read_all_task
from .operations import read_task
from .operations import remove_task
from .operations import update_task

app = FastAPI()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/tasks")
def get_tasks() -> List[TaskResponse]:
    return read_all_task()


@app.get("/v2/tasks")
def get_tasks_v2(db: Session = Depends(get_db)) -> List[TaskV2Response]:
    all_task = db.query(Tasks).all()
    if all_task is None:
        raise HTTPException(status_code=404, detail="No tasks found!")
    return all_task


@app.get("/task/{task_id}")
def get_task(task_id: int) -> Optional[TaskResponse]:
    task = read_task(task_id)
    if task is None:
        raise HTTPException(status_code=404, detail="Task not found!")
    return task


@app.post("/task")
def add_task(task: Task) -> TaskResponse:
    return create_task(task)


@app.post("/v2/task")
def add_task_v2(task: TaskV2, db: Session = Depends(get_db)) -> TaskV2Response:
    new_task = Tasks(**task.model_dump())
    db.add(new_task)
    db.commit()
    db.refresh(new_task)
    return TaskV2Response(**new_task.__dict__)


@app.put("/task/{task_id}")
def change_task(task_id: int, task_data: Task) -> TaskResponse:
    changed_task = update_task(task_id, task_data)
    if not changed_task:
        raise HTTPException(status_code=404, details=f"Task id: {task_id} not found")
    return changed_task


@app.delete("/task/{task_id}")
def delete_task(task_id: int) -> TaskResponse:
    task_to_remove = remove_task(task_id)
    if not task_to_remove:
        raise HTTPException(status_code=404, details=f"Task id: {task_id} not found")
    return TaskResponse(**task_to_remove)
