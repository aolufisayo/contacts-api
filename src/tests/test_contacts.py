import json
import pytest
from app.api import crud

def test_create_new_contact(test_app, monkeypatch):
    test_request_payload = {"first_name": "bruno", "last_name": "alves"}
    test_response_payload = {"id": 1, "first_name": "bruno", "last_name": "alves"}

    async def mock_post(payload):
        return 1

    monkeypatch.setattr(crud, "post", mock_post)

    response = test_app.post("/contacts/", data=json.dumps(test_response_payload),)
    assert response.status_code == 201
    assert response.json() == test_response_payload

def test_create_new_contact_inavlid_json(test_app):
    response = test_app.post("/contacts/", data=json.dumps({"first_name": "1"}))
    assert response.status_code == 422

def test_read_contact(test_app, monkeypatch):
    test_data = {"id": 1, "first_name": "johhny", "last_name": "bravo"}

    async def mock_get(id):
        return test_data

    monkeypatch.setattr(crud, "get", mock_get)

    response = test_app.get("/contacts/1")
    assert response.status_code == 200
    assert response.json() == test_data

def test_read_contact_incorrect_id(test_app, monkeypatch):
    async def mock_get(id):
        return None

    monkeypatch.setattr(crud, "get", mock_get)

    response = test_app.get("/contacts/1000")
    assert response.status_code == 404
    assert response.json()["detail"] == "Contact Not Found"

    response = test_app.get("/contacts/0")
    assert response.status_code == 422

def test_read_all_contacts(test_app, monkeypatch):
    test_data = [
        {"id": 1, "first_name": "joseph", "last_name": "hughes"},
        {"id": 2, "first_name": "bridget", "last_name": "jones"}
    ]

    async def mock_get_all():
        return test_data

    monkeypatch.setattr(crud, "get_all", mock_get_all)

    response = test_app.get("/contacts/")
    assert response.status_code == 200
    assert response.json() == test_data


def test_update_contact(test_app, monkeypatch):
    test_update_data = {"id": 1, "first_name": "agbede", "last_name": "lukman"}

    async def mock_get(id):
        return True

    monkeypatch.setattr(crud, "get", mock_get)

    async def mock_put(id, payload):
        return 1

    monkeypatch.setattr(crud, "put", mock_put)
    response = test_app.put("/contacts/1/", data= json.dumps(test_update_data))
    assert response.status_code == 200
    assert response.json() == test_update_data

@pytest.mark.parametrize(
    "id, payload, status_code",
    [
        [1, {}, 422],
        [1, {"first_name": "bola"}, 422],
        [1000,{"first_name": "agbede", "last_name": "lukman"}, 404],
        [1, {"last_name": "lukman"}, 422],
        [0, {"first_name": "agbede", "last_name": "lukman"}, 422]
    ]
)
def test_update_contact_invalid_json(test_app, monkeypatch, id, payload, status_code):
    async def mock_get(id):
        return None

    monkeypatch.setattr(crud, "get", mock_get)

    response = test_app.put(f"/contacts/{id}/", data=json.dumps(payload),)
    assert response.status_code == status_code

def test_remove_contact(test_app, monkeypatch):
    test_data = {"id": 1, "first_name": "agbede", "last_name": "lukman"}

    async def mock_get(id):
        return test_data

    monkeypatch.setattr(crud, "get", mock_get)
    async def mock_delete(id):
        return id

    monkeypatch.setattr(crud, "delete", mock_delete)
    response = test_app.delete("/contacts/1/")
    assert response.status_code == 200
    assert response.json() == test_data

def test_remove_contact_incorrect_id(test_app, monkeypatch):
    async def mock_get(id):
        return None

    monkeypatch.setattr(crud, "get", mock_get)

    response = test_app.delete("/contacts/1000/")
    assert response.status_code == 404
    assert response.json()["detail"] == "Contact Not Found"

    response = test_app.delete("/contacts/0/")
    assert response.status_code == 422