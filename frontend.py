import streamlit as st
import requests

st.set_page_config(
    page_title="Python Assistant",
    page_icon="🐍"
)

st.title("🐍 Python Programming Assistant")

if "history" not in st.session_state:
    st.session_state.history = []

question = st.chat_input(
    "Ask a Python question..."
)

if question:

    st.session_state.history.append(
        ("user", question)
    )

    response = requests.post(
        "http://127.0.0.1:8000/ask",
        json={
            "question": question
        }
    )

    answer = response.json()

    st.session_state.history.append(
        ("assistant",
         answer["answer"])
    )

for role, msg in st.session_state.history:

    with st.chat_message(role):
        st.markdown(msg)