# app.py
import streamlit as st

# ------------------------------
# Page Config
# ------------------------------
st.set_page_config(
    page_title="Welcome Test",
    page_icon="👋",
    layout="centered",
)

# ------------------------------
# Welcome Page
# ------------------------------
st.title("Diasense AI assistant!")
st.write("This is the AI assistant for Diabetes with american book 2026 (care of diabetes).")

# Optional button
if st.button("Click Me"):
    st.success("Deployment works! 🎉")

# Footer
st.markdown("---")
st.markdown("Made with ❤️ using Streamlit")
