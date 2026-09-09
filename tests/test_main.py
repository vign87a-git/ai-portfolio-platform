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

def test_generate_content_success(monkeypatch):
    monkeypatch.setenv("GEMINI_API_KEY", "test-key-123")
    
    class MockResponse:
        text = "Hello from Gemini 3.6 Flash!"

    class MockModels:
        def generate_content(self, model, contents):
            assert model == "gemini-3.6-flash"
            assert contents == "Hello AI"
            return MockResponse()

    class MockClient:
        def __init__(self, api_key):
            assert api_key == "test-key-123"
            self.models = MockModels()

    monkeypatch.setattr("google.genai.Client", MockClient)
    
    response = client.post("/generate", json={"text": "Hello AI"})
    assert response.status_code == 200
    json_data = response.json()
    assert json_data == {"reply": "Hello from Gemini 3.6 Flash!"}

def test_generate_content_quota_exceeded(monkeypatch):
    monkeypatch.setenv("GEMINI_API_KEY", "test-key-123")

    class MockModels:
        def generate_content(self, model, contents):
            raise Exception("429 RESOURCE_EXHAUSTED. Your prepayment credits are depleted.")

    class MockClient:
        def __init__(self, api_key):
            self.models = MockModels()

    monkeypatch.setattr("google.genai.Client", MockClient)
    
    response = client.post("/generate", json={"text": "Hello AI"})
    assert response.status_code == 200
    json_data = response.json()
    assert "error" in json_data
    assert "credits depleted" in json_data["error"]


