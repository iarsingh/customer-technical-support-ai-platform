from fastapi.testclient import TestClient
from csupport.main import app

client = TestClient(app)


def test_answers_and_refuses():
    hit = client.post("/ask", json={"question": 'Why do SSO failures happen with clock skew?'}).json()
    assert hit["answered"] is True
    assert hit["citation"] == "sso.md"
    miss = client.post("/ask", json={"question": 'movie times'}).json()
    assert miss["answered"] is False


def test_empty_is_refused():
    assert client.post("/ask", json={"question": " "}).status_code == 422
