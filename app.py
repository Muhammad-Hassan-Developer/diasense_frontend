# app.py
import streamlit as st

# ------------------------------
# Page Config
# ------------------------------
st.set_page_config(
    page_title="Diasense AI Assistant",
    page_icon="🩺",
    layout="wide",
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
            border-radius: 10px;
            background-color: #2E86C1;
            color: white;
            font-weight: bold;
        }
        .stButton>button:hover {
            background-color: #1B4F72;
            color: white;
        }
    </style>
""", unsafe_allow_html=True)

# ------------------------------
# Sidebar
# ------------------------------
with st.sidebar:
    st.image("https://cdn-icons-png.flaticon.com/512/3774/3774299.png", width=100)
    st.title("Diasense AI")
    st.markdown("---")
    st.write("AI-powered Diabetes Assistant")

    if st.button("🗑 Clear Chat"):
        st.session_state.messages = []
        st.rerun()

    st.markdown("---")
    st.caption("Demo Version | Upwork Portfolio")

# ------------------------------
# Header Section
# ------------------------------
st.markdown("""
    <h1 style='text-align: center; color: #1B4F72;'>🩺 Diasense AI Assistant</h1>
    <p style='text-align: center; font-size:18px;'>Guideline-Based Diabetes AI Chatbot</p>
""", unsafe_allow_html=True)

st.markdown("---")

# ------------------------------
# Session State for Chat History
# ------------------------------
if "messages" not in st.session_state:
    st.session_state.messages = []

# ------------------------------
# Chat Container
# ------------------------------
chat_container = st.container()

with chat_container:
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

# ------------------------------
# Chat Input
# ------------------------------
user_input = st.chat_input("Ask a diabetes-related question...")

if user_input:
    # Store User Message
    st.session_state.messages.append({"role": "user", "content": user_input})

    with st.chat_message("user"):
        st.markdown(user_input)

    # Simulated AI Response (Replace with Backend API)
    bot_response = f"Thank you for your question. \n\nYou asked: **{user_input}** \n\nThis is a demo AI-generated response."

    st.session_state.messages.append({"role": "assistant", "content": bot_response})

    with st.chat_message("assistant"):
        st.markdown(bot_response)

# ------------------------------
# Footer
# ------------------------------
st.markdown("---")
st.markdown(
    "<div style='text-align:center;'>Made with ❤️ using Streamlit | © 2026 Diasense AI</div>",
    unsafe_allow_html=True
)