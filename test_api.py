from fastapi.testclient import TestClient
from app.main import app

# Initialize the internal tester (bypasses Windows network blocks)
client = TestClient(app)

print("====== Internal API Verification ======")

# 1. Test the root endpoint
print("\n[1/2] Testing Connection to API Root...")
response_home = client.get("/")
print("Server Status Response:", response_home.json())

# 2. Test the /ask endpoint with a real question
print("\n[2/2] Sending Question to /ask endpoint...")
question_to_ask = "What is the main topic of this document?"

print(f"Asking: '{question_to_ask}' (Connecting to Gemini, please wait...)\n")
response_ask = client.get(f"/ask?question={question_to_ask}")

print("================ ANSWER ================")
if response_ask.status_code == 200:
    print("AI Response:", response_ask.json()["answer"])
else:
    print(f"Error {response_ask.status_code}:", response_ask.json())
print("========================================")