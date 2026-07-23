import streamlit as st
import requests
import re

BACKEND_URL = "https://talkright.onrender.com/chat"

st.set_page_config(
    page_title="TalkRight",
    page_icon="💬",
    layout="centered"
)

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@500;700&family=Inter:wght@400;500;600&display=swap');

.stApp {
    background: radial-gradient(circle at top, #161A36 0%, #0B0D1F 60%);
    color: #E8E9F3;
    font-family: 'Inter', sans-serif;
}

#MainMenu, footer, header {visibility: hidden;}

/* Reduce default top padding so content isn't floating far down */
.block-container {
    padding-top: 2.5rem !important;
    max-width: 720px;
}

.talkright-title {
    font-family: 'Space Grotesk', sans-serif;
    font-weight: 700;
    font-size: 2.2rem;
    background: linear-gradient(90deg, #7C83FD, #B4B8FF);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    margin-bottom: 0.1rem;
}

.talkright-caption {
    color: #9598B8;
    font-size: 0.95rem;
    margin-bottom: 2rem;
    border-bottom: 1px solid #262B4D;
    padding-bottom: 1.2rem;
}

/* Chat bubbles — FIXED: auto height + more padding so content never overflows */
[data-testid="stChatMessage"] {
    background-color: #171B34;
    border-radius: 16px;
    padding: 1rem 1.1rem;
    margin-bottom: 0.7rem;
    border: 1px solid #262B4D;
    box-shadow: 0 2px 8px rgba(0,0,0,0.25);
    height: auto !important;
    overflow: visible !important;
}

/* Ensure inner content wraps properly and doesn't get clipped */
[data-testid="stChatMessage"] > div {
    overflow: visible !important;
    height: auto !important;
}

/* User message — subtle accent tint to differentiate from bot */
[data-testid="stChatMessage"]:has([data-testid="stChatMessageAvatarUser"]) {
    background-color: #1D2145;
    border: 1px solid #363B6E;
}

/* Chat input — force-remove any red/invalid outline, always show accent color */
[data-testid="stChatInput"] {
    border-color: #262B4D !important;
}
[data-testid="stChatInput"] textarea {
    background-color: #171B34 !important;
    color: #E8E9F3 !important;
    border: 1px solid #363B6E !important;
    border-radius: 12px !important;
    box-shadow: none !important;
    padding: 10px 16px !important;
}
[data-testid="stChatInput"] textarea:focus {
    border: 1px solid #7C83FD !important;
    box-shadow: 0 0 0 2px rgba(124,131,253,0.25) !important;
}
[data-testid="stChatInput"] button {
    background-color: #7C83FD !important;
    border-radius: 10px !important;
}

/* Correction badge */
.correction-badge {
    display: inline-block;
    background-color: rgba(245, 185, 113, 0.12);
    border: 1px solid #F5B971;
    color: #F5B971;
    padding: 5px 12px;
    border-radius: 20px;
    font-size: 0.82rem;
    font-weight: 500;
    margin-bottom: 8px;
}

.reply-text {
    font-size: 0.98rem;
    color: #E8E9F3;
    line-height: 1.55;
}
</style>
""", unsafe_allow_html=True)

st.markdown('<p class="talkright-title">💬 TalkRight</p>', unsafe_allow_html=True)
st.markdown('<p class="talkright-caption">Chat naturally in English — I\'ll help you speak like a native, one message at a time.</p>', unsafe_allow_html=True)

if "messages" not in st.session_state:
    st.session_state.messages = []

def render_bot_message(content):
    correction_match = re.search(r"Correction:\s*(.*?)(?:\n|$)", content)
    reply_match = re.search(r"Reply:\s*(.*)", content, re.DOTALL)

    if correction_match and reply_match:
        correction_text = correction_match.group(1).strip()
        reply_text = reply_match.group(1).strip()
        st.markdown(f'<div class="correction-badge">✏️ {correction_text}</div>', unsafe_allow_html=True)
        st.markdown(f'<div class="reply-text">{reply_text}</div>', unsafe_allow_html=True)
    else:
        st.write(content)

for message in st.session_state.messages:
    avatar = "🧑" if message["role"] == "user" else "💬"
    with st.chat_message(message["role"], avatar=avatar):
        if message["role"] == "assistant":
            render_bot_message(message["content"])
        else:
            st.write(message["content"])

user_message = st.chat_input("Type your message...")

if user_message:
    with st.chat_message("user", avatar="🧑"):
        st.write(user_message)
    st.session_state.messages.append({"role": "user", "content": user_message})

    with st.spinner("Thinking..."):
        response = requests.post(
            BACKEND_URL,
            json={"user_input": user_message}
        )
        bot_reply = response.json()["message"]

    with st.chat_message("assistant", avatar="💬"):
        render_bot_message(bot_reply)
    st.session_state.messages.append({"role": "assistant", "content": bot_reply})