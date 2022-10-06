import pytest
from app import schemas
from .database import client, session



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

def test_login_user(client):
    client.post(
        "/users/", 
        json={
            "username": "test", 
            "email": "test@mail.ru", 
            "password": "password"
        }
    )
    response = client.post("/login", data={"username": "test@mail.ru", "password": "password"})
    assert response.status_code == 200



