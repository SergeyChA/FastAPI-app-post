import pytest
from jose import jwt
from app import schemas
from app.config import settings


def test_root(client):
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello, Sergey!!!"}


def test_create_user(client):
    response = client.post(
        "/users/",
        json={
            "username": "test",
            "email": "test@mail.ru",
            "password": "password"
        }
    )
    new_user = schemas.UserOut(**response.json())
    assert new_user.email == "test@mail.ru"
    assert response.status_code == 201


def test_login_user(test_user, client):
    response = client.post(
        "/login",
        data={
            "username": test_user["email"],
            "password": test_user["password"]
        }
    )
    login = schemas.Token(**response.json())
    payload = jwt.decode(
        login.access_token,
        settings.secret_key,
        algorithms=[settings.algorithm]
    )
    id = payload.get("user_id")
    assert id == test_user["id"]
    assert login.token_type == "bearer"
    assert response.status_code == 200


@pytest.mark.parametrize("email, password, status_code", [
    ('wrong_email@mail.ru', 'password', 403),
    ('test@mail.ru', 'wrong_password', 403),
    ('wrongemail@mail.ru', 'wrong_password', 403),
    (None, 'password', 422),
    ('test@mail.ru', None, 422)
    ]
)
def test_incorrect_login(test_user, email, password, status_code, client):
    response = client.post(
        "/login",
        data={
            "username": email,
            "password": password
        }
    )
    assert response.status_code == status_code
