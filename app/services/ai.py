from app.config import GROQ_API_KEY
import requests
from app.database import get_messages, save_message
import json
from app.services.tools import tool_functions, tools
SYSTEM_PROMPT = {
    "role": "system",
    "content": "You are a friendly AI programming tutor. Explain programming concepts simply. Teach step by step and encourage the user to think instead of just giving answers. When a calculation is required, use the calculate tool. When the current time is requested, use the get_time tool. After receiving a tool result, use that result directly to give the final answer. Do not recalculate the result yourself."
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
        "model": "openai/gpt-oss-20b",
        "messages": messages,
        "tools": tools,
        "tool_choice": "auto",
        "temperature": 0
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

        if e.response is not None:
            print("GROQ ERROR:", e.response.text)

        return "Sorry, I'm having trouble connecting to the AI service, please try again in few"

    print("STATUS:", response.status_code)
    print("RESPONSE:", response.text)

    result = response.json()

    tool_rounds = 0

    executed_tool_calls = set()

    while True:
        tool_rounds += 1

        if tool_rounds > 3:
            reply = "I wasn't able to complete that request."
            break

        assistant_message = result["choices"][0]["message"]

        tool_calls = assistant_message.get("tool_calls")

        if not tool_calls:
            reply = assistant_message.get("content", "")
            break

        messages.append(assistant_message)
        for tool_call in tool_calls:
            function_name = tool_call["function"]["name"]

            try:
                arguments = json.loads(
                    tool_call["function"]["arguments"]
                )

            except json.JSONDecodeError:
                tool_result = "The tool arguments were invalid."

            else:
                call_key = f"{function_name}:{json.dumps(arguments, sort_keys=True)}"

                if call_key in executed_tool_calls:
                    data["tool_choice"] = "none"
                    break

                executed_tool_calls.add(call_key)

                tool_function = tool_functions.get(function_name)

                if tool_function:
                    tool_result = tool_function(**arguments)
                    print("TOOL RESULT:", tool_result)
                else:
                    tool_result = f"Unknown tool: {function_name}"
            messages.append({
                "role": "tool",
                "tool_call_id": tool_call["id"],
                "content": str(tool_result)
            })

            print("TOOL MESSAGE ADDED")

        data["messages"] = messages

        response = requests.post(
            url,
            headers=headers,
            json=data,
            timeout=30
        )

        print("SENDING NEXT REQUEST")

        response.raise_for_status()

        result = response.json()

        print(
            "AGENT RESPONSE:",
            json.dumps(result, indent=2)
        )

    save_message(conversation_id, "user", message)
    save_message(conversation_id, "assistant", reply)

    return reply