from fastapi import APIRouter
from fastapi.responses import HTMLResponse

from app.models.chat import ChatRequest
from app.services.ai import ask_ai
from app.database import create_conversation, get_conversations, get_messages, delete_conversation


router = APIRouter()


@router.get("/", response_class=HTMLResponse)
def home():
    with open("static/index.html", "r", encoding="utf-8") as file:
        return file.read()

@router.post("/chat")
def chat(chat_request: ChatRequest):
    reply = ask_ai(
        chat_request.message,
        chat_request.conversation_id
        )

    return {
        "user": chat_request.message,
        "reply": reply
    }


@router.post("/conversation")
def new_conversation():
    conversation_id = create_conversation()

    return {
        "conversation_id": conversation_id
    }

@router.get("/conversation/{conversation_id}")
def get_conversation(conversation_id: int):
    messasges = get_messages(conversation_id)

    return {
        "conversation_id": conversation_id,
        "messages": messasges
    }

@router.get("/conversations")
def conversation():
    return get_conversations()

@router.delete("/conversation/{conversation_id}")
def remove_conversation(conversation_id: int):
    delete_conversation(conversation_id)

    return {
        "message": "Conversation deleted"
    }
