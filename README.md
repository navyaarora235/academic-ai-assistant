# Academic Document Query Service

A FastAPI backend and Streamlit front end that lets users upload an academic PDF and ask questions about it, answered by Gemini 2.5 Flash.

[![Streamlit App](https://img.shields.io/badge/Live_Demo-Streamlit-FF4B4B?style=for-the-badge&logo=streamlit)](https://academic-ai-assistant.streamlit.app/)

## How it works

1. The user uploads a PDF and types a question (through the Streamlit UI or `POST /query`).
2. `pypdf` extracts the text from the PDF.
3. The full text and the question go to Gemini in one prompt, which is told to answer only from the document.
4. The API returns JSON with the question and the answer.
5. The backend is deployed on Render; the Streamlit front end calls it over HTTP.

## Features

- REST endpoint (`POST /query`) with input validation and error handling.
- Clean split between the API (`main.py`), the PDF and Gemini logic (`pipeline.py`), and the UI (`streamlit_app.py`).
- Tests using FastAPI's `TestClient` (`test_api.py`).

## Limitations

- The whole document text is sent in a single prompt, so very long PDFs may exceed the model's context limit.
- Scanned PDFs without selectable text are not supported.
- This is prompt-based Q&A, not RAG: there is no chunking or retrieval.

## Run locally

```
pip install -r requirements.txt
# set GEMINI_API_KEY in a .env file
uvicorn app.main:app --reload
streamlit run streamlit_app.py
pytest
```

## Project structure

```
academic-ai-assistant/
├── app/
│   ├── main.py          # FastAPI routes
│   └── pipeline.py      # PDF text extraction and Gemini call
├── streamlit_app.py     # Streamlit front end
├── test_api.py          # Tests
├── sample.pdf           # Sample document
├── requirements.txt
└── README.md
```
