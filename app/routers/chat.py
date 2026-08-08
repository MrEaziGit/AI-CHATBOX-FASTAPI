from fastapi import APIRouter
from fastapi.responses import HTMLResponse

from app.models.chat import ChatRequest
from app.services.ai import ask_ai, conversation

router = APIRouter()


@router.get("/", response_class=HTMLResponse)
def home():
    with open("static/index.html", "r", encoding="utf-8") as file:
        return file.read()

@router.post("/chat")
def chat(chat_request: ChatRequest):
    reply = ask_ai(chat_request.message)

    return {
        "user": chat_request.message,
        "reply": reply
    }

@router.post("/reset")
def reset():
    conversation.clear()
    conversation.append({
        "role": "system",
        "content": "You are a friendly AI programming tutor. Explain programming concepts simply. Teach step by step and encourage the user to think instead of just giving answers."
    })
    return {
        "message": "conversation reset successfully"
    }