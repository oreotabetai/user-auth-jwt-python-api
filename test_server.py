from server import app
from fastapi.testclient import TestClient


client = TestClient(app)


def test_root():
    response = client.get("/")
    assert response.status_code == 200


def test_register_user():
    response = client.post(
        "/register"
    )
    assert response.status_code == 200


# [TODO]: Connect Testing Database
# Return 422 by invalid userdata
def test_login():
    response = client.post(
        "/login",
        json={"id": "test", "password": "test"}
    )
    assert response.status_code == 422


# Return 403 by invalid authorization
def test_read_current_user():
    response = client.get("/my")
    assert response.status_code == 403
