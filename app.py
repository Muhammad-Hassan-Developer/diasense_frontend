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
st.title("👋 Welcome to Streamlit Deployment Test!")
st.write("This is a simple page to test deployment of your Streamlit app.")

# Optional button
if st.button("Click Me"):
    st.success("Deployment works! 🎉")

# Footer
st.markdown("---")
st.markdown("Made with ❤️ using Streamlit")
