#Academic Document Query Microservice

A production-ready, modular backend web service built with **FastAPI** and **Gemini 2.5-Flash** that allows users to query academic PDF documents via structured REST API endpoints.

#Technical Architecture
- **Separation of Concerns:** Deconstructed monolithic script architecture into a clean split between the API router service (`main.py`) and the textual extraction pipeline (`pipeline.py`).
- **Native Text Parsing:** Processes local document contexts seamlessly utilizing `pypdf`.
- **Isolated Integration Testing:** Implements an automated backend test suite using FastAPI's `TestClient` framework to guarantee endpoint integrity independently of browser/network constraints.

#Project Structure
```text
academic-ai-assistant/
│
├── app/                  
│   ├── main.py           # FastAPI Web Routing Gateway
│   └── pipeline.py       # PDF Processing & Gemini Integration Engine
│
├── requirements.txt      # Dependency Registry
└── test_api.py           # Integration Test Suite
