from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_create_employee():
    response = client.post("/employees", json={
        "name": "John Doe",
        "address": "New York",
        "salary": 50000,
        "age": 30
    })
    assert response.status_code == 200
    assert response.json()["name"] == "John Doe"

def test_get_employees():
    response = client.get("/employees")
    assert response.status_code == 200

def test_get_employee_not_found():
    response = client.get("/employees/9999")
    assert response.status_code == 404

def test_delete_employee():
    emp = client.post("/employees", json={
        "name": "Jane Doe",
        "address": "LA",
        "salary": 60000,
        "age": 28
    }).json()
    response = client.delete(f"/employees/{emp['id']}")
    assert response.status_code == 200
