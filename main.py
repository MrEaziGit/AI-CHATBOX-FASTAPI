from fastapi import FastAPI
from pydantic import BaseModel
import requests
from fastapi.middleware.cors import CORSMiddleware
import os
from dotenv import load_dotenv

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://127.0.0.1:5500"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
    
)
conversation = [
    {
        "role": "system",
        "content": "You are a friendly AI programming tutor. Explain programming concepts simply. Teach step by step and encourage the user to think instead of just giving answers."
    }
]


class ChatRequest(BaseModel):
    message: str

load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")

print("KEY:", GROQ_API_KEY)

def ask_ai(message: str):
    url = "https://api.groq.com/openai/v1/chat/completions"

    headers = {
        "Authorization": f"Bearer {GROQ_API_KEY}",
        "Content-Type": "application/json"
    }

    conversation.append({
        "role": "user",
        "content": message
    })
    print(conversation)

    data = {
        "model": "llama-3.1-8b-instant",
        "messages": conversation
    }

    response = requests.post(url, headers=headers, json=data)
    print("STATUS:", response.status_code)
    print("RESPONSE:", response.text)



    reply = response.json()["choices"][0]["message"]["content"]

    conversation.append({
        "role": "assistant",
        "content": reply
    }) 
    return reply

@app.get("/")
def home():
    return {"message": "AI Chatbot is running"}


@app.post("/chat")
def chat(chat_request: ChatRequest):
    reply = ask_ai(chat_request.message)

    return {
        "user": chat_request.message,
        "reply": reply
    }