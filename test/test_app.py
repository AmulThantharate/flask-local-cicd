import pytest
from app import app


@pytest.fixture
def client():
    app.config["TESTING"] = True
    from app import tasks
    tasks.clear()
    with app.test_client() as client:
        yield client


def test_health(client):
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json == {"status": "ok"}


def test_create_task(client):
    response = client.post("/tasks", json={"title": "Deploy flask app"})
    assert response.status_code == 201
    assert response.json == {"id": 1, "title": "Deploy flask app"}


def test_reject_empty_title(client):
    response = client.post("/tasks", json={"title": ""})
    assert response.status_code == 400
    assert response.json == {"message": "title is required"}
