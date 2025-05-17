from fastapi.testclient import TestClient
from app import app

cliet = TestClient(app) 

def test_hello_message():
    response = cliet.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello World how're you"}