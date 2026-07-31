# Academic Document Query Microservice

A production-ready, modular backend web service built with **FastAPI** and **Gemini 2.5-Flash** that allows users to query academic PDF documents via structured REST API endpoints and an interactive web UI.

[![Streamlit App](https://img.shields.io/badge/Live_Demo-Streamlit-FF4B4B?style=for-the-badge&logo=streamlit)](https://academic-ai-assistant.streamlit.app/)

## Technical Architecture

* **Separation of Concerns:** Deconstructed monolithic script architecture into a clean split between the API router service (`main.py`), the textual extraction pipeline (`pipeline.py`), and a lightweight client interface (`streamlit_app.py`).
* **Native Text Parsing:** Processes local document contexts seamlessly utilizing `pypdf`.
* **Isolated Integration Testing:** Implements an automated backend test suite using FastAPI's `TestClient` framework to guarantee endpoint integrity independently of browser/network constraints.

## Project Structure

```text
academic-ai-assistant/
│
├── app/
│   ├── main.py        # FastAPI Web Routing Gateway
│   └── pipeline.py    # PDF Processing & Gemini Integration Engine
│
├── .gitignore
├── README.md
├── requirements.txt   # Dependency Registry
├── sample.pdf         # Test Document
├── streamlit_app.py   # Streamlit Client Interface
└── test_api.py        # Integration Test Suite
