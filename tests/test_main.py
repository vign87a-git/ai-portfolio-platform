import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert "AI Portfolio Engine" in response.text

def test_generate_missing_api_key(monkeypatch):
    monkeypatch.delenv("GEMINI_API_KEY", raising=False)
    response = client.post("/generate", json={"text": "Hello"})
    assert response.status_code == 200
    json_data = response.json()
    assert "error" in json_data
