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
# Header
# ------------------------------
st.title("🩺 Diasense AI Assistant")
st.caption("Based on American Diabetes Care Guidelines 2026")

st.write(
    "Welcome! This AI assistant helps answer diabetes-related "
    "questions using guideline-based knowledge."
)

# ------------------------------
# Demo Button
# ------------------------------
if st.button("Test Deployment"):
    st.success("Frontend deployed successfully! 🎉")

# ------------------------------
# Footer
# ------------------------------
st.markdown("---")
st.markdown("Made with ❤️ using Streamlit")