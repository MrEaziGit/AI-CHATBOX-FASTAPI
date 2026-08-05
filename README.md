# AI Chatbot with FastAPI & Groq

A conversational AI chatbot built with **Python**, **FastAPI**, **JavaScript**, **HTML**, and **CSS**, powered by the **Groq LLM API**.

This project demonstrates frontend-backend communication, REST APIs, prompt engineering, modular FastAPI architecture, and AI integration.

---

 # Features

*  AI-powered conversations using the Groq API
*  FastAPI backend
*  Responsive HTML/CSS frontend
*  Real-time communication with Fetch API
*  Markdown rendering for AI responses
*  System prompts for AI behavior customization
*  Modular project structure (routers, services, models, config)
*  CORS-enabled frontend and backend integration

---

# Tech Stack

* Python
* FastAPI
* JavaScript (ES6)
* HTML5
* CSS3
* Groq API
* Git & GitHub

---

Project Structure

```
project1/
│
├── app/
│   ├── main.py
│   ├── routers/
│   ├── services/
│   ├── models/
│   └── config.py
│
├── static/
│   ├── index.html
│   ├── design.css
│   └── script.js
│
├── requirements.txt
└── README.md
```

---

# Installation

Clone the repository:

```bash
git clone https://github.com/MrEaziGit/AI-CHATBOX-FASTAPI.git
```

Navigate into the project:

```bash
cd AI-CHATBOX-FASTAPI
```

Create a virtual environment:

```bash
python -m venv venv
```

Activate it:

**Windows**

```bash
venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Create a `.env` file and add your Groq API key:

```
GROQ_API_KEY=your_api_key_here
```

Run the application:

```bash
uvicorn app.main:app --reload
```

Open your browser:

```
http://127.0.0.1:8000/
```

---

## 📸 Preview

*Add screenshots or a short GIF of the chatbot here.*

---

## 📚 What I Learned

* Building REST APIs with FastAPI
* Frontend and backend integration
* Prompt engineering
* Working with LLM APIs
* Git and GitHub workflow
* Debugging API requests and CORS issues
* Organizing scalable Python projects

---

# Future Improvements

* User authentication
* Chat history database
* Syntax highlighting
* Streaming AI responses
* File uploads
* Deployment to Vercel/Render

---

Author

**Olayinka Israel**

GitHub: https://github.com/MrEaziGit
