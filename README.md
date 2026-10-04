# Internship Assistant Chatbot

## Project Overview

The Internship Assistant is a web-based chatbot designed to provide instant answers to common internship-related questions.

The system uses a retrieval-based chatbot engine with predefined input patterns and a structured JSON knowledge base. A Flask REST API connects the chatbot engine to the web interface.

## System Architecture

User
  ↓
Chat Interface
  ↓
Flask REST API
  ↓
Chatbot Engine
  ↓
Pattern Matching
  ↓
Knowledge Base
  ↓
Response
  ↓
User

## Core Features

- Instant chatbot responses
- Retrieval-based response system
- Predefined input patterns
- Structured knowledge base
- Internship-related question handling
- Multiple predefined intents
- Keyword and sentence similarity matching
- Fallback handling for unknown questions
- REST API communication
- Responsive web interface
- Suggested questions
- Typing indicator
- Message timestamps
- Copy response functionality
- User feedback controls
- API error handling
- Mobile-friendly interface
- Professional user interface

## Supported Topics

The chatbot currently handles questions related to:

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

## Technology Stack

### Backend

- Python
- Flask
- Flask-CORS

### Chatbot Engine

- Python
- JSON knowledge base
- Pattern matching
- Keyword similarity
- Sentence similarity
- Retrieval-based responses

### Frontend

- HTML5
- CSS3
- JavaScript
- Responsive design
```
## Project Structure

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
├── .gitignore
└── README.md
```
## API

### POST /api/chat

The frontend sends a user question to the Flask API.

Example request:

{
  "message": "What are your internship timings?"
}

Example response:

{
  "response": "The internship working hours are Monday to Friday, from 10:00 AM to 6:00 PM."
}

## Accuracy and Reliability

The chatbot uses predefined knowledge rather than generating unsupported information. This makes responses predictable and suitable for frequently asked internship questions.

When a question does not sufficiently match the available knowledge, the chatbot uses a fallback response instead of inventing an answer.

## User Engagement

The interface provides:

- Suggested questions
- Clear user and assistant message separation
- Typing feedback
- Response timestamps
- Copy response functionality
- Response feedback controls
- Responsive design
- Clear input and send controls

## Error Handling

The application handles unsuccessful API requests and displays a user-friendly message when the chatbot service cannot be reached.

## Running the Application

Activate the virtual environment and run:

python -m app.main

Then open:

http://127.0.0.1:5000

## Future Enhancements

Possible future improvements include:

- LLM integration
- Retrieval-Augmented Generation (RAG)
- Conversation memory
- Vector database
- Document-based knowledge retrieval
- Authentication
- Analytics
- Production WSGI deployment

## Task Completion

This implementation satisfies the major requirements of the chatbot task:

1. AI-powered chatbot design
2. Instant responses
3. Retrieval-based response system
4. Predefined input patterns
5. Website integration
6. Accuracy and user-engagement improvements
