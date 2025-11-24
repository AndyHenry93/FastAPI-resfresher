import pytest
from fastapi.testclient import TestClient

from src.task_manager_app.main import app
from src.task_manager_app.operations import read_all_task

client = TestClient(app)


def test_endpoint_read_all_tasks(test_task):
    response = client.get("/tasks")
    assert response.status_code == 200
    assert response.json() == test_task


@pytest.mark.parametrize(
    "id, status_code, list_value",
    [(1, 200, 0), (5, 404, 0)],
    ids=["test 200 sstatus code", "test 404 status code"],
)
def test_endpoint_get_task(test_task, id, status_code, list_value):
    response = client.get(f"/task/{id}")
    assert response.status_code == status_code
    if status_code == 200:
        assert response.json() == test_task[list_value]


@pytest.mark.parametrize(
    "title,desc, status, id, expected_status",
    [
        ("task five", "Go food shopping", "In-progress", 5, 200),
        ("task six", 56, "In-progress", 5, 200),
    ],
    ids=["test 200 create task", "test 404 create task"],
)
def test_endpoint_create_task(title, desc, status, id, expected_status):
    task = {
        "title": title,
        "description": desc,
        "status": status,
        "id": id,
    }
    response = client.post("/task", json=task)
    assert response.status_code == expected_status
    assert response.json() == {**task, "id": id}
    assert len(read_all_task()) == id
