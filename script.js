
const input = document.getElementById("msg");
const sendBtn = document.getElementById("sendBtn");


input.addEventListener("keydown", function(event) {
    if (event.key === "Enter") {
        send();
    }
});

async function send() {

    let message = input.value;

    if (!message) return;

    let chatBox = document.getElementById("chatBox");

    chatBox.innerHTML += `
        <div class="msg user">
            You: ${message}
        </div>
    `;

    input.value = "";

    let typing = document.createElement("div");
    typing.className = "msg bot";
    typing.textContent = "AI is typing...";
    chatBox.appendChild(typing);

    sendBtn.disabled = true;

    let res = await fetch("http://127.0.0.1:8000/chat", {
    method: "POST",
    headers: {
        "Content-Type": "application/json"
    },
    body: JSON.stringify({
        message: message
    })
});

    let data = await res.json();

    typing.textContent = "Bot: " + data.reply;

    sendBtn.disabled = false;
    chatBox.scrollTop = chatBox.scrollHeight;
}

