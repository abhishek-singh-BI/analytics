import streamlit as st
import requests

# URL for your FastAPI backend
API_URL = "http://127.0.0.1:8000/chat"

# Streamlit frontend layout
st.title("Chat with Amazon AI Assistant")

# Text input for the user message
user_input = st.text_input("Ask your question:")

# If the user input exists, call the FastAPI backend
if user_input:
    try:
        # Sending a request to the FastAPI backend with the user's message
        response = requests.post(API_URL, json={"message": user_input})

        # Extract the response from FastAPI
        if response.status_code == 200:
            result = response.json()
            st.write(f"**AI Response**: {result['response']}")
        else:
            st.error("Error communicating with the server")
    except requests.exceptions.RequestException as e:
        st.error(f"Request failed: {e}")
