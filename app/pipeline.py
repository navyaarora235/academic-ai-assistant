import os
from pypdf import PdfReader
from google import genai

def query_academic_pdf(user_question: str) -> str:
    pdf_filename = "sample.pdf"
    api_key = os.getenv("GOOGLE_API_KEY")
    
    # 1. Extract text natively from the PDF file
    reader = PdfReader(pdf_filename)
    document_text = ""
    for page in reader.pages:
        document_text += page.extract_text() + "\n"
        
    if not document_text.strip():
        return "Error: The PDF appears to be empty."

    # 2. Connect to standalone Google Client
    client = genai.Client(api_key=api_key)
    
    # 3. Create structural engineering prompt for Gemini
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