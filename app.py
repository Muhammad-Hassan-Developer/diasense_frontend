# app.py
import streamlit as st

# ------------------------------
# Page Config
# ------------------------------
st.set_page_config(
    page_title="Diasense AI Assistant",
    page_icon="🩺",
    layout="centered",
)

# ------------------------------
# Custom CSS Styling
# ------------------------------
st.markdown("""
    <style>
        .main {
            background-color: #f5f7fa;
        }
        .stChatMessage {
            border-radius: 15px;
            padding: 10px;
        }
        .stButton>button {
            border-radius: 8px;
            background-color: #2E86C1;
            color: white;
            font-weight: 600;
        }
        .stButton>button:hover {
            background-color: #1B4F72;
            color: white;
        }
        .center-header {
            text-align: center;
            margin-bottom: 10px;
        }
        .title-text {
            font-size: 32px;
            font-weight: bold;
            color: #1B4F72;
        }
        .subtitle-text {
            font-size: 16px;
            color: #555;
        }
    </style>
""", unsafe_allow_html=True)

# ------------------------------
# ------------------------------
# Centered Header
# ------------------------------
st.markdown("""
    <div class='center-header'>
        <div class='title-text'>🩺 Diasense AI Assistant</div>
        <div class='subtitle-text'>Guideline-Based Diabetes AI Chatbot</div>
    </div>
""", unsafe_allow_html=True)

st.markdown("---")

# ------------------------------
# Session State
# ------------------------------
if "messages" not in st.session_state:
    st.session_state.messages = []

# ------------------------------
# Chat Messages
# ------------------------------
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# ------------------------------
# Chat Input
# ------------------------------
user_input = st.chat_input("Ask a diabetes-related question...")

if user_input:
    st.session_state.messages.append({"role": "user", "content": user_input})

    with st.chat_message("user"):
        st.markdown(user_input)

    bot_response = f"Thank you for your question.\n\nYou asked: **{user_input}**\n\nThis is a demo AI-generated response."

    st.session_state.messages.append({"role": "assistant", "content": bot_response})

    with st.chat_message("assistant"):
        st.markdown(bot_response)

# ------------------------------
# Footer
# ------------------------------
st.markdown("---")
st.markdown(
    "<div style='text-align:center; font-size:13px; color:gray;'>© 2026 Diasense AI | Built with Streamlit</div>",
    unsafe_allow_html=True
)
