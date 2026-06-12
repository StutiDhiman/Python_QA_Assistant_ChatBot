import pandas as pd

from langchain_core.documents import Document
from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings


print("Loading CSV files...")

questions = pd.read_csv(
    "data/Questions.csv",
    encoding="latin1",
    low_memory=False
)

answers = pd.read_csv(
    "data/Answers.csv",
    encoding="latin1",
    low_memory=False
)

print("Questions:", len(questions))
print("Answers:", len(answers))

documents = []

# Demo ke liye first 5000 questions
questions = questions.head(5000)

for _, q in questions.iterrows():

    qid = q["Id"]

    related_answers = answers[
        answers["ParentId"] == qid
    ]

    if len(related_answers) == 0:
        continue

    best_answer = related_answers.sort_values(
        by="Score",
        ascending=False
    ).iloc[0]

    content = f"""
Question Title:
{q['Title']}

Question Body:
{q['Body']}

Best Answer:
{best_answer['Body']}
"""

    documents.append(
        Document(
            page_content=content,
            metadata={
                "question_id": int(qid)
            }
        )
    )

print("Documents created:", len(documents))

embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

vectorstore = FAISS.from_documents(
    documents,
    embeddings
)

vectorstore.save_local("vectorstore")

print("FAISS index saved!")