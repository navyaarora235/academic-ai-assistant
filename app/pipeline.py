import io
import os
from pypdf import PdfReader
from google import genai

def query_academic_pdf(pdf_bytes: bytes, user_question: str) -> str:
    pdf_file = io.BytesIO(pdf_bytes)
    reader = PdfReader(pdf_file)
    document_text = ""
    
    for page in reader.pages:
        text = page.extract_text()
        if text:
            document_text += text + "\n"
        
    if not document_text.strip():
        return "Error: Could not extract text from the uploaded PDF."
    api_key = os.getenv("GEMINI_API_KEY") or os.getenv("GOOGLE_API_KEY")

    client = genai.Client(api_key=api_key)
    
    prompt = f"""You are a helpful academic research assistant. 
Use the following extracted document context to answer the user's question precisely. 
If the context does not contain the answer, state that you cannot find it.

Context:
{document_text}

Question: {user_question}
Answer:"""

    response = client.models.generate_content(
        model='gemini-2.5-flash',
        contents=prompt,
    )
    
    return response.text