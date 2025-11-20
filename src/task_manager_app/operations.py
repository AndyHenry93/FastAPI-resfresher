import csv
from typing import Any
from typing import Dict
from typing import List
from typing import Optional

from .models import Task
from .models import TaskResponse
from .utils import columns
from .utils import database_name
from .utils import get_next_id
from .utils import write_task_to_db


def read_all_task() -> List[TaskResponse]:
    with open(database_name()) as csv_file:
        reader = csv.DictReader(
            csv_file,
        )
        return [TaskResponse(**row) for row in reader]


def read_task(task_id: int) -> Optional[TaskResponse]:
    with open(database_name()) as csv_file:
        reader = csv.DictReader(
            csv_file,
        )
        for row in reader:
            if int(row["id"]) == task_id:
                return TaskResponse(**row)
        return None


def create_task(task: Task) -> TaskResponse:
    id = get_next_id()
    new_task = TaskResponse(id=id, **task.model_dump())
    write_task_to_db(new_task)
    return new_task


def update_task(task_id: int, task_data: Task) -> Optional[TaskResponse]:
    all_tasks = read_all_task()
    updated_task: Optional[TaskResponse] = None

    for i, db_task in enumerate(all_tasks):
        if db_task.id == task_id:
            updated_task = db_task.model_copy(update=task_data.model_dump())
            all_tasks[i] = updated_task

    with open(database_name(), mode="w", newline="") as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=columns())
        writer.writeheader()
        for task in all_tasks:
            writer.writerow(task.model_dump())

    if updated_task:
        return updated_task
    return None


def remove_task(task_id: int) -> Optional[Dict[str, Any]]:
    deleted_task: Optional[TaskResponse] = None
    all_tasks = read_all_task()

    with open(database_name(), mode="w", newline="") as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=columns())
        writer.writeheader()
        for task in all_tasks:
            if task.id == task_id:
                deleted_task = task
                continue
            writer.writerow(task.model_dump())

    if deleted_task:
        removed_task = deleted_task.model_dump()
        return removed_task
    return None
