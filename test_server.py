from server import app
from fastapi.testclient import TestClient


client = TestClient(app)


def test_root():
    response = client.get("/")
    assert response.status_code == 200


# [TODO]: Connect Testing Database (Returns an error code for now)
def test_register_user():
    response = client.post(
        "/register"
    )
    assert response.status_code == 400


def test_login():
    response = client.post(
        "/login",
        json={"id": "test", "password": "test"}
    )
    assert response.status_code == 422


def test_read_current_user():
    response = client.get("/my")
    assert response.status_code == 403
