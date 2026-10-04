# 🤖 Internship Assistant Chatbot

A professional web-based chatbot developed as part of the **CodeAlpha Internship Program — Task 4: Making a Chatbot**.

The Internship Assistant provides instant responses to common internship-related questions using a **retrieval-based chatbot engine**, predefined input patterns, and a structured knowledge base.

---

## 📌 Project Overview

The **Internship Assistant Chatbot** is designed to help interns quickly find information related to their internship.

Instead of manually searching through instructions or documentation, users can simply ask a question through the chatbot interface and receive an appropriate response.

The system combines:

- A responsive web-based chat interface
- Flask REST API
- Retrieval-based chatbot engine
- Predefined question patterns
- Structured JSON knowledge base
- Similarity-based response matching
- Fallback handling for unknown questions

---

## ✨ Features

### 💬 Chatbot Features

- Instant responses
- Predefined input patterns
- Retrieval-based response generation
- Keyword and sentence similarity matching
- Multiple internship-related topics
- Reliable predefined responses
- Fallback response for unsupported questions

### 🎨 User Interface

- Modern professional UI
- Responsive design
- User and assistant message distinction
- Suggested questions
- Typing indicator
- Message timestamps
- Copy response functionality
- 👍 / 👎 response feedback
- Mobile-friendly interface
- Clean and accessible chat experience

### 🛡️ Reliability

- Structured knowledge base
- Controlled responses
- API error handling
- Input length limitation
- Fallback responses instead of unsupported information

---

## 🧠 Supported Topics

The chatbot currently supports questions related to:

- Internship timings
- Internship duration
- Internship tasks
- Eligibility
- Application process
- Required documents
- Attendance
- Leave
- Internship certificate
- Internship completion
- Mentor guidance
- Technical support
- Project submission
- Submission deadlines
- Greetings
- Thank-you messages
- Goodbye messages

---

## 🏗️ System Architecture

```
                  ┌──────────────────┐
                  │       User       │
                  └────────┬─────────┘
                           │
                           ▼
                  ┌──────────────────┐
                  │   Chat Interface │
                  │   HTML/CSS/JS    │
                  └────────┬─────────┘
                           │
                           ▼
                  ┌──────────────────┐
                  │    Flask API     │
                  │   /api/chat      │
                  └────────┬─────────┘
                           │
                           ▼
                  ┌──────────────────┐
                  │  Chatbot Engine  │
                  │    Python        │
                  └────────┬─────────┘
                           │
                           ▼
                  ┌──────────────────┐
                  │ Pattern Matching │
                  │   & Similarity   │
                  └────────┬─────────┘
                           │
                           ▼
                  ┌──────────────────┐
                  │ Knowledge Base   │
                  │      JSON        │
                  └────────┬─────────┘
                           │
                           ▼
                  ┌──────────────────┐
                  │    Response      │
                  └──────────────────┘
```
---

## 🛠️ Technology Stack

- **Backend:** Python, Flask, Flask-CORS
- **Chatbot Engine:** Python, JSON Knowledge Base, Pattern Matching, Keyword Similarity, Sentence Similarity
- **Frontend:** HTML5, CSS3, JavaScript
- **Data Storage:** JSON
- **Development Environment:** Python Virtual Environment

---

## 📁 Project Structure

```
Chatbot/
│
├── app/
│   ├── chatbot/
│   │   ├── __init__.py
│   │   └── engine.py
│   │
│   ├── knowledge/
│   │   └── knowledge.json
│   │
│   ├── routes/
│   │   ├── __init__.py
│   │   └── chat.py
│   │
│   ├── __init__.py
│   └── main.py
│
├── frontend/
│   └── index.html
│
├── requirements.txt
├── README.md
├── TASK4_STATUS.md
└── .gitignore
```

## 🔄 How It Works

User Question  
↓  
Frontend Request  
↓  
`POST /api/chat`  
↓  
Flask API  
↓  
Pattern Matching  
↓  
Best Matching Intent  
↓  
Knowledge Base Response  
↓  
Response Displayed in Chat

## 🌐 API

### `POST /api/chat`

**Request:**
```json
{
  "message": "What are your internship timings?"
}

Response:

{
  "response": "The internship working hours are Monday to Friday, from 10:00 AM to 6:00 PM."
}
⚙️ Installation
git clone https://github.com/shaikh-abdul-basit436/CodeAlpha_Chatbot.git
cd CodeAlpha_Chatbot
python -m venv .venv
Windows PowerShell
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
▶️ Run the Application
python -m app.main

Open:

http://127.0.0.1:5000

🎯 Example Questions
What are your internship timings?
How long is the internship?
What tasks do I have?
What documents are required?
How do I apply?
How is attendance recorded?
Can I take leave?
Will I get a certificate?
How do I submit my project?
What is the submission deadline?
I need technical help.
✨ Features
🔍 Retrieval-based intent matching
⚡ Fast and predictable responses
📚 Controlled JSON knowledge base
🛡️ Fallback response for unknown questions
💡 Suggested questions
⌨️ Typing indicator
🕒 Message timestamps
📋 Copy response button
👍👎 Feedback controls
📱 Responsive interface
🔐 Basic API error handling
📊 Accuracy & Reliability

The chatbot uses predefined patterns and a controlled knowledge base instead of generating unsupported information. This provides:

Consistent responses
Easy knowledge-base maintenance
Reduced risk of incorrect information
Fast response times
🚀 Future Enhancements
Large Language Model integration
RAG pipeline
Vector database
Document-based retrieval
Conversation memory
Context-aware responses
Authentication
Chat analytics
Admin knowledge-base management
Production WSGI deployment
📚 Documentation

Detailed implementation information is available in:

TASK4_STATUS.md

🎓 Internship Task

Program: CodeAlpha Internship
Task: Task 4 — Making a Chatbot
Status: ✅ Completed

Requirements Addressed
Requirement	Implementation
AI Chatbot	Internship Assistant Chatbot
API	Flask REST API
Retrieval	Predefined patterns
Knowledge Base	JSON
Website Integration	Responsive web interface
Accuracy	Pattern & similarity matching
User Engagement	Suggestions & interactive UI
Reliability	Fallback & error handling
👨‍💻 Author

Shaikh Abdul Basit
B.Sc. Information Technology
Software & Cloud Computing Enthusiast

GitHub: https://github.com/shaikh-abdul-basit436
Email: abdulbasitshaikh436@gmail.com

🔗 Repository

https://github.com/shaikh-abdul-basit436/CodeAlpha_Chatbot

⭐ If you found this project useful, consider giving it a star!

CodeAlpha Internship — Task 4: Internship Assistant Chatbot
Status: Completed ✅

Copyright © 2026 Shaikh Abdul Basit. All rights reserved.
