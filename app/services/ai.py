import requests
from app.config import GROQ_API_KEY

conversation = [
    {
        "role": "system",
        "content": "You are a friendly AI programming tutor. Explain programming concepts simply. Teach step by step and encourage the user to think instead of just giving answers."
    }
]



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
