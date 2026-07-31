from fastapi import FastAPI, HTTPException, UploadFile, File, Form
from dotenv import load_dotenv
from app.pipeline import query_academic_pdf

load_dotenv()

app = FastAPI(
    title="Academic AI Assistant API",
    description="A production-ready RAG backend microservice leveraging Gemini 2.5."
)

@app.get("/")
def home():
    return {"status": "Operational", "service": "Academic Research Assistant"}

@app.post("/query")
async def ask_document(
    question: str = Form(...),
    file: UploadFile = File(...)
):
    if not question.strip():
        raise HTTPException(status_code=400, detail="Question cannot be empty.")
    
    try:
        pdf_bytes = await file.read()
        
        ai_response = query_academic_pdf(pdf_bytes, question)
        return {"question": question, "answer": ai_response}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))