# 🤖 CodeAlpha Chatbot

A web-based chatbot developed as part of the **CodeAlpha Internship – Task 4: Making a Chatbot**.

The chatbot provides users with quick and relevant answers to common internship-related questions using a **Python Flask backend, structured knowledge base, and retrieval-based response system**.

---

## 🛠️ Technology Stack

- **Backend:** Python, Flask, Flask-CORS
- **Chatbot Engine:** Python, JSON Knowledge Base, Pattern Matching, Keyword Similarity, Sentence Similarity
- **Frontend:** HTML5, CSS3, JavaScript
- **Data Storage:** JSON
- **Development Environment:** Python Virtual Environment

---

## 📁 Project Structure

```text
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

⚙️ Installation
Clone the Repository:
```
git clone https://github.com/shaikh-abdul-basit436/CodeAlpha_Chatbot.git
```

Move into the Project Folder:
````
cd CodeAlpha_Chatbot
````

Create Virtual Environment:
```
python -m venv .venv
```

Activate Virtual Environment
Windows PowerShell
```
.venv\Scripts\Activate.ps1
```

Linux / macOS:
```
source .venv/bin/activate
```

Install Dependencies:
```
pip install -r requirements.txt
```

▶️ Run the Application
Start the Flask application using:
```
python -m app.main
```

Open your browser and visit:
```
http://127.0.0.1:5000
```

```
🤖 Chatbot Flow
User
   ↓
Enter Question
   ↓
Chatbot Frontend
   ↓
POST /api/chat
   ↓
Flask Backend
   ↓
Chatbot Engine
   ↓
Knowledge Base
   ↓
Match User Query
   ↓
Generate Response
   ↓
Display Answer
```
```
## 🌐 API

**Endpoint:** `POST /api/chat`

```json
{
  "message": "What are the internship timings?"
}

Response:
{
  "response": "The internship follows the timings provided by CodeAlpha."
}
```
## 💬 Example Questions
The chatbot handles questions about:
- Internship timings and duration
- Tasks and eligibility
- Application and required documents
- Attendance and leave
- Mentor and technical support
- Project submission and deadlines
- Certificate and completion
- General greetings and thanks
--- 
## 📊 Reliability
- Structured knowledge base
- Query and pattern matching
- Relevant predefined responses
- Unsupported-query handling
- API and server error handling
---
## 📸 Screens
- Chatbot Interface
- Suggested Questions
- Chat Conversation
- Bot Responses
- Feedback Controls
- Mobile View
---
## 🔮 Future Enhancements
- LLM and RAG Integration
- Database Integration
- User Authentication
- Conversation History
- Admin Dashboard
- Voice and Multilingual Support
- Analytics
- Cloud Deployment
---

## 🎓 Internship Task
- This project was developed for:
- CodeAlpha Internship
- Task: Task 4 – Making a Chatbot
- Requirements
- Requirement	Status
- Create a chatbot	✅ Completed
- Develop chatbot interface	✅ Completed
- Implement backend API	✅ Completed
- Create knowledge base	✅ Completed
- Implement query matching	✅ Completed
- Handle user queries	✅ Completed
- Add error handling	✅ Completed
- Create responsive UI	✅ Completed

---

## 🔮 Future Enhancements

- User Login & Registration
- Admin Dashboard
- Leaderboard
- Question Management System
- Database Integration (MySQL)
- Performance Analytics
- Certificate Generation
- Multiplayer Quiz
- Cloud Deployment

---

## 👨‍💻 Developer

**Shaikh Abdul Basit**

Second-Year B.Sc. Information Technology Student

GitHub:
https://github.com/shaikh-abdul-basit436

Email:
abdulbasitshaikh436@gmail.com

---

## ⭐ Support

If you found this project useful, consider giving it a ⭐ on GitHub.

It helps support the project and encourages future improvements.

---

## Copyright

© 2026 Shaikh Abdul Basit. All rights reserved.

This project is provided for viewing and educational purposes only.
