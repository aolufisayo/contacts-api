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

