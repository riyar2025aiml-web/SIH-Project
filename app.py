import streamlit as st
import google.generativeai as genai
from dotenv import load_dotenv
import os

load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

genai.configure(api_key=GEMINI_API_KEY)

st.set_page_config(page_title="Digital Learning Chatbot")

model = genai.GenerativeModel("gemini-2.5-flash")

st.title("Digital Learning Platform Chatbot")
st.markdown("Helping rural school students in **Nabha** with interactive learning.")

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

user_input = st.chat_input("Ask me any question (Math, Science, English...)")

if user_input:
    st.session_state.chat_history.append({"role": "user", "text": user_input})

    try:
        response = model.generate_content(user_input)
        bot_reply = response.text
    except Exception as e:
        bot_reply = f"⚠️ Error: {e}"

    st.session_state.chat_history.append({"role": "bot", "text": bot_reply})

for msg in st.session_state.chat_history:
    if msg["role"] == "user":
        st.chat_message("user").write(msg["text"])
    else:
        st.chat_message("assistant").write(msg["text"])
