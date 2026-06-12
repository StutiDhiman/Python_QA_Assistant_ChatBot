from dotenv import load_dotenv

load_dotenv()

from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_groq import ChatGroq


embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

db = FAISS.load_local(
    "vectorstore",
    embeddings,
    allow_dangerous_deserialization=True
)

retriever = db.as_retriever(
    search_kwargs={"k": 3}
)

llm = ChatGroq(
    model="llama-3.3-70b-versatile",
    temperature=0
)


def ask_question(question):

    docs = retriever.invoke(question)

    context = "\n\n".join(
        [doc.page_content for doc in docs]
    )

    prompt = f"""
You are a Python tutor.

Answer only using the provided context.

If context is insufficient,
say:
'I could not find a grounded answer.'

Context:
{context}

Question:
{question}
"""

    response = llm.invoke(prompt)

    return {
        "answer": response.content,
        "sources": [
            d.metadata["question_id"]
            for d in docs
        ]
    }