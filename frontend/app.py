import streamlit as st
import requests

# Page configuration
st.set_page_config(
    page_title="TalkRight",
    page_icon="💬",
    layout="centered"
)

st.title("💬 TalkRight")
st.caption("Chat naturally in English - I'll help you speak like a native, one message at a time.")

# Storing chat history
if "message" not in st.session_state:
    st.session_state.messages = []

# Showing past chat
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

# User input
user_message = st.chat_input("Type your message...")

# Handling user inpur and calling backend
if user_message:

    # showing user's message
    with st.chat_message("user"):
        st.write(user_message)

    # saving user message to history
    st.session_state.messages.append({"role": "user", "content": user_message})

    #calling backend
    with st.spinner("Thinking..."):

        response = requests.post(
            "http://127.0.0.1:8000/chat",
            json={"user_input": user_message}
        )

        bot_reply = response.json()["message"]

        # Showing bot reply on screen
        with st.chat_message("assistant"):
            st.write(bot_reply)

        # Storing bot reply in chat history
        st.session_state.messages.append({"role": "assistant", "content": bot_reply})