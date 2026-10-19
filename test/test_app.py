import os
import pytest
from app import app


@pytest.fixture
def client():
    app.config["TESTING"] = True

    with app.test_client() as client:
        yield client


def test_endpoint(client):
    response = client.get("/health")
    assert response.status_code == 200
    assert response.get_json() == {
        "status": "ok",
        "environment": os.environ.get("APP_ENV", "dev"),
    }


def test_health_status_is_ok(client):
    response = client.get("/health")

    data = response.get_json()
    assert data["status"] == "ok"


def test_health_returns_environment(client):
    response = client.get("/health")

    data = response.get_json()
    assert "environment" in data
    assert isinstance(data["environment"], str)
