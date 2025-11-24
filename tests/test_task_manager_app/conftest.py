import csv
from typing import Any
from typing import Dict
from typing import List
from unittest.mock import patch

import pytest

from src.task_manager_app.utils import columns


@pytest.fixture()
def test_database_file() -> str:
    return "test_task.csv"


@pytest.fixture()
def test_task_csv() -> List[Dict[str, str]]:
    return [
        {
            "title": "Task One",
            "description": "Task out the trash",
            "status": "Incomplete",
            "id": 1,
        },
        {
            "title": "Task two",
            "description": "Wash the car",
            "status": "In Progress",
            "id": 2,
        },
        {
            "title": "Task Three",
            "description": "clean the bathroom",
            "status": "Incomplete",
            "id": 3,
        },
        {
            "title": "Task Four",
            "description": "clean the bedroom",
            "status": "Incomplete",
            "id": 4,
        },
    ]


@pytest.fixture()
def test_task(test_task_csv) -> List[Dict[str, Any]]:
    return [{**task_json, "id": int(task_json["id"])} for task_json in test_task_csv]


@pytest.fixture(autouse=True)
def create_test_db(tmp_path, test_task_csv):
    database_file_loc = tmp_path / "test_task.csv"
    print("path", database_file_loc)
    with patch(
        "task_manager_app.utils.database_name", return_value=str(database_file_loc)
    ):
        with open(database_file_loc, mode="w", newline="") as csv_file:
            writer = csv.DictWriter(csv_file, fieldnames=columns())
            writer.writeheader()
            for task in test_task_csv:
                writer.writerow(task)
        yield
