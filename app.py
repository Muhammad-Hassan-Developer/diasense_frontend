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
# Title
# ------------------------------
st.title("🩺 Diasense AI Assistant")
st.caption("Diabetes AI Chatbot (Demo Mode)")

# ------------------------------
# Session State for Chat History
# ------------------------------
if "messages" not in st.session_state:
    st.session_state.messages = []

# ------------------------------
# Display Chat History
# ------------------------------
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# ------------------------------
# Chat Input
# ------------------------------
user_input = st.chat_input("Ask a diabetes-related question...")

if user_input:
    # Save user message
    st.session_state.messages.append({"role": "user", "content": user_input})
    
    with st.chat_message("user"):
        st.markdown(user_input)

    # ------------------------------
    # Temporary Bot Response (Replace with Backend API Later)
    # ------------------------------
    bot_response = f"You asked: '{user_input}'.\n\nThis is a demo chatbot response."

    # Save bot response
    st.session_state.messages.append({"role": "assistant", "content": bot_response})

    with st.chat_message("assistant"):
        st.markdown(bot_response)

# ------------------------------
# Footer
# ------------------------------
st.markdown("---")
st.markdown("Made with ❤️ using Streamlit")
