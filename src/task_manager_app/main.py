from typing import List
from typing import Optional

from fastapi import FastAPI
from fastapi import HTTPException

from .models import Task
from .models import TaskResponse
from .operations import create_task
from .operations import read_all_task
from .operations import read_task
from .operations import remove_task
from .operations import update_task

app = FastAPI()


@app.get("/tasks")
def get_tasks() -> List[TaskResponse]:
    return read_all_task()


@app.get("/task/{task_id}")
def get_task(task_id: int) -> Optional[TaskResponse]:
    task = read_task(task_id)
    if task is None:
        raise HTTPException(status_code=404, detail="Task not found!")
    return task


@app.post("/task")
def add_task(task: Task) -> TaskResponse:
    return create_task(task)


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
