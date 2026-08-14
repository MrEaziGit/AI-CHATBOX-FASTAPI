from app.config import GROQ_API_KEY
import requests 
from app.database import get_messages, save_message

SYSTEM_PROMPT = {
    "role": "system",
    "content": "You are a friendly AI programming tutor. Explain programming concepts simply. Teach step by step and encourage the user to think instead of just giving answers."
}


def ask_ai(message: str, conversation_id: int):
    url = "https://api.groq.com/openai/v1/chat/completions"

    headers = {
        "Authorization": f"Bearer {GROQ_API_KEY}",
        "Content-Type": "application/json"
    }

    messages = [SYSTEM_PROMPT]

    history = get_messages(conversation_id)
    messages.extend(history)

    messages.append({
        "role": "user",
        "content": message
    })

    data = {
        "model": "llama-3.1-8b-instant",
        "messages": messages
    }

    try:
        response = requests.post(
            url,
            headers=headers,
            json=data,
            timeout=30
        )

        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print("AI REQUEST ERROR:", e)
        return "Sorry, I'm having trouble connecting to the AI service, please try again in few"
    print("STATUS:", response.status_code)
    print("RESPONSE:", response.text)

    reply = response.json()["choices"][0]["message"]["content"]

    save_message(conversation_id,"user", message)

    save_message(conversation_id,"assistant", reply)

    return reply