import streamlit as st
import requests

BACKEND_URL = "http://0.0.0.0:8000/ask"

st.set_page_config(page_title="Ai mental health therapist", layout="wide")
st.title("Safespace - Ai mental health therapist")

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

userinput = st.text_input("What's on your mind today?", key="user_input")

if userinput:
    st.session_state.chat_history.append({"role": "user", "content": userinput})
    try:
        res = requests.post(BACKEND_URL, json={"message": userinput})
        res.raise_for_status()
        data = res.json()
        print("Backend response:", data)   # Debug
        answer = data.get("response", "No response field in backend reply")
    except Exception as e:
        answer = f"Backend error: {e}"

    st.session_state.chat_history.append({"role": "assistant", "content": answer})

# Display messages
for msg in st.session_state.chat_history:
    role = "👤 User:" if msg["role"] == "user" else "🤖 Assistant:"
    st.markdown(f"**{role}** {msg['content']}")
