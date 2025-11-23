from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_root():
    response = client.get("/")
    assert response.status_code in [200, 404]


def test_get_posts_empty():
    response = client.get("/post")
    assert response.status_code == 200
    assert response.json() == []


def test_create_post():
    response = client.post("/post", json={"body": "This is a test post"})
    assert response.status_code == 201
    data = response.json()
    assert data["body"] == "This is a test post"
    assert "id" in data
