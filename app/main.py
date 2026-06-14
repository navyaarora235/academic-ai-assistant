from fastapi import FastAPI, HTTPException
from dotenv import load_dotenv
from app.pipeline import query_academic_pdf

# Load API keys from the .env file
load_dotenv()

# Initialize the FastAPI Web Framework
app = FastAPI(
    title="Academic AI Assistant API",
    description="A production-ready RAG backend microservice leveraging Gemini 2.5."
)

@app.get("/")
def home():
    return {"status": "Operational", "service": "Academic Research Assistant"}

@app.get("/ask")
def ask_document(question: str):
    if not question.strip():
        raise HTTPException(status_code=400, detail="Question cannot be empty.")
    
    try:
        # Call the function from pipeline.py
        ai_response = query_academic_pdf(question)
        return {"question": question, "answer": ai_response}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))