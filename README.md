# Python Programming Q&A Assistant

## Overview

Python Programming Q&A Assistant is a Retrieval-Augmented Generation (RAG) application built using the Stack Overflow Python Questions & Answers dataset.

The system retrieves relevant Python discussions from Stack Overflow and generates grounded answers using a Large Language Model (LLM). The application is designed to help data science learners and Python developers obtain accurate answers to programming-related questions.

---

## Features

* Retrieval-Augmented Generation (RAG) Pipeline
* FastAPI Backend
* Streamlit Frontend
* FAISS Vector Database
* HuggingFace Embeddings
* Groq Llama 3.3 70B Integration
* Grounded Question Answering
* REST API Endpoints
* Automated API Testing using Pytest

---

## Dataset

Dataset Used:

Stack Overflow — Python Questions & Answers

Source:
https://www.kaggle.com/datasets/stackoverflow/pythonquestions

Files Used:

* Questions.csv
* Answers.csv
* Tags.csv

---

## Architecture

```text
User
 │
 ▼
Streamlit Frontend
 │
 ▼
FastAPI Backend
 │
 ▼
FAISS Retriever
 │
 ▼
StackOverflow Knowledge Base
 │
 ▼
Groq Llama 3.3 70B
 │
 ▼
Grounded Answer
```

---

## Tech Stack

### Backend

* FastAPI
* LangChain
* FAISS
* HuggingFace Embeddings
* Groq API

### Frontend

* Streamlit

### Data Processing

* Pandas
* BeautifulSoup

### Testing

* Pytest

---

## Project Structure

```text
python-qa-assistant/
│
├── app/
│   ├── ingest.py
│   ├── rag.py
│   ├── main.py
│
├── data/
│   ├── Questions.csv
│   ├── Answers.csv
│   └── Tags.csv
│
├── tests/
│   └── test_api.py
│
├── vectorstore/
│
├── frontend.py
├── evaluation.md
├── requirements.txt
├── README.md
└── .env.example
```

---

## Installation

### Clone Repository

```bash
git clone <repository-url>
cd python-qa-assistant
```

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Virtual Environment

Windows:

```bash
venv\Scripts\activate
```

Linux / Mac:

```bash
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Environment Variables

Create a `.env` file:

```env
GROQ_API_KEY=your_groq_api_key
```

Example file:

`.env.example`

```env
GROQ_API_KEY=your_groq_api_key
```

---

## Build Vector Database

Run:

```bash
python app/ingest.py
```

This will:

* Load Stack Overflow data
* Clean HTML content
* Create embeddings
* Generate FAISS vector index

---

## Run Backend

```bash
uvicorn app.main:app --reload
```

API Documentation:

```text
http://127.0.0.1:8000/docs
```

---

## Run Frontend

```bash
streamlit run frontend.py
```

Frontend URL:

```text
http://localhost:8501
```

---

## API Endpoints

### Health Check

```http
GET /health
```

Response:

```json
{
  "status": "healthy"
}
```

---

### Ask Question

```http
POST /ask
```

Request:

```json
{
  "question": "How do I reverse a list in Python?"
}
```

Response:

```json
{
  "answer": "...",
  "sources": [...]
}
```

---

## Testing

Run:

```bash
pytest
```

The API was evaluated using multiple Python-related questions.

Detailed results are available in:

```text
evaluation.md
```

---

## Sample Questions

* How do I reverse a list in Python?
* What is list comprehension?
* Difference between tuple and list?
* How do generators work?
* How can I convert PDF to JPEG on Windows?
* What CI tools can be used for Python projects?

---

## Future Improvements

* Hybrid Retrieval (BM25 + Vector Search)
* Conversation Memory
* Source Citation UI
* Re-ranking Models
* Redis Caching
* Qdrant/Pinecone Vector Database
* User Authentication
* Feedback Collection System

---

## Scaling for 100+ Concurrent Users

To support production workloads:

* Async FastAPI endpoints
* Redis caching layer
* Horizontal scaling using containers
* Managed vector databases (Qdrant/Pinecone)
* Load balancing
* Monitoring and observability
* Request queueing for heavy workloads

---

## Deployment Note

The application was fully implemented and tested locally.

Due to memory limitations of free-tier hosting platforms when loading the embedding model and FAISS index simultaneously, deployment remains a future enhancement. All instructions required to run the application locally are included in this repository.

## Author

Analytics Vidhya AI Engineer Assessment Submission

Built using:
FastAPI, LangChain, FAISS, HuggingFace Embeddings, Groq Llama 3.3 70B, and Streamlit.
