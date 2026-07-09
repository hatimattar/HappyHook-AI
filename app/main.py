from app.services.gemini_service import chat_with_ai
from pydantic import BaseModel
from fastapi import FastAPI

class ChatRequest(BaseModel):
    message: str

app = FastAPI(
    title="HappyHook AI",
    version="1.0.0"
)

@app.get("/")
def home():
    return {
        "message": "HappyHook AI is running 🚀"
    }

@app.post("/chat")
def chat(request: ChatRequest):
    reply = chat_with_ai(request.message)
    return {
        "reply": reply
    }