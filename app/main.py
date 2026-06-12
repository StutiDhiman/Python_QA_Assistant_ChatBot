from fastapi import FastAPI
from pydantic import BaseModel

from app.rag import ask_question

app = FastAPI()


class AskRequest(BaseModel):
    question: str


@app.get("/health")
def health():

    return {
        "status": "healthy"
    }


@app.post("/ask")
def ask(req: AskRequest):

    return ask_question(
        req.question
    )