from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_create_task():
    response = client.post("/tasks/", json={"title": "Test Task"})
    assert response.status_code == 200
    assert response.json()["title"] == "Test Task"

def test_get_tasks():
    response = client.get("/tasks/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_update_task_status():
    create_response = client.post("/tasks/", json={"title": "Test Task"})
    task_id = create_response.json()["id"]
    update_response = client.patch(f"/tasks/{task_id}", json={"completed": True})
    assert update_response.status_code == 200
    assert update_response.json()["completed"] == True

def test_delete_task():
    create_response = client.post("/tasks/", json={"title": "Task to Delete"})
    task_id = create_response.json()["id"]
    delete_response = client.delete(f"/tasks/{task_id}")
    assert delete_response.status_code == 200
    assert delete_response.json()["detail"] == "Task deleted"
