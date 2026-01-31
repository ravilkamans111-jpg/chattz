import pytest
from fastapi.testclient import TestClient
from src.main import app

client = TestClient(app)

def test_create_chat():

    response = client.post("/chats/", json={"title": "Test Chat"})
    assert response.status_code == 200
    data = response.json()
    assert data["title"] == "Test Chat"
    assert "id" in data
