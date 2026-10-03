from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_root():
       r = client.get("/")
       assert r.status_code == 200
       assert r.json()["status"] == "Operational"

def test_empty_question_rejected():
       with open("sample.pdf", "rb") as f:
           r = client.post("/query", data={"question": "  "},
                           files={"file": ("sample.pdf", f, "application/pdf")})
       assert r.status_code == 400

def test_query_returns_answer():
       with open("sample.pdf", "rb") as f:
           r = client.post("/query", data={"question": "What is the main topic?"},
                           files={"file": ("sample.pdf", f, "application/pdf")})
       assert r.status_code == 200
       assert "answer" in r.json()