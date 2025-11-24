import csv

from .models import TaskResponse


def database_name():
    return "src\\task_manager_app\\task.csv"


def columns():
    return ["id", "title", "description", "status"]


def get_next_id():
    try:
        with open(database_name()) as csv_file:
            reader = csv.DictReader(
                csv_file,
            )
            max_id = max(int(row["id"]) for row in reader)
            return max_id + 1
    except (FileNotFoundError, ValueError):
        return 1


def write_task_to_db(task: TaskResponse):
    with open(database_name(), "a+", newline="") as csv_file:
        writer = csv.DictWriter(
            csv_file,
            fieldnames=columns(),
        )
        writer.writerow(task.model_dump())
