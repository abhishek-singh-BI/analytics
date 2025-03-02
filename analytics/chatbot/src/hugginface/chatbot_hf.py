import requests
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from dotenv import load_dotenv
import os

# Initialize FastAPI app
app = FastAPI()

# Load environment variables
load_dotenv(
    "/Users/abhisheksingh/VS_Code_Projects/analytics/analytics/analytics/chatbot/chatbot.env"
)

# Get Hugging Face API key
hf_api_key = os.getenv("HUGGINGFACE_API_KEY")

# Hugging Face API endpoint (using a fine-tuned conversational model)
HF_API_URL = "https://api-inference.huggingface.co/models/microsoft/DialoGPT-medium"

# Restricted topics
RESTRICTED_TOPICS = ["pricing", "policy", "confidential"]
SUPPORT_EMAIL = "support@example.com"

# Banned words
BANNED_WORDS = ["shit", "dark net", "illegal", "hack"]


# Request model
class ChatRequest(BaseModel):
    message: str


# Function to filter inappropriate content
def filter_response(response: str) -> str:
    if any(word in response.lower() for word in BANNED_WORDS):
        return "I'm sorry, but I can't provide a response to that."
    return response


# Function to get response from Hugging Face
def get_hf_response(user_input: str) -> str:
    if any(topic in user_input.lower() for topic in RESTRICTED_TOPICS):
        return f"Please reach out to {SUPPORT_EMAIL} for more details."

    headers = {"Authorization": f"Bearer {hf_api_key}"}
    prompt = f"The following is a conversation with a helpful AI assistant. The assistant is polite, professional, and avoids inappropriate content.\n\nUser: {user_input}\nAI:"
    payload = {"inputs": prompt}

    try:
        response = requests.post(HF_API_URL, headers=headers, json=payload)
        response.raise_for_status()
        generated_text = response.json()[0]["generated_text"]
        return filter_response(generated_text)
    except Exception as e:
        print(f"Error occurred: {e}")
        return f"Sorry, I am unable to process the request right now. Error: {str(e)}"


# API endpoint to process user requests
@app.post("/chat")
def chat(request: ChatRequest):
    try:
        response = get_hf_response(request.message)
        return {"response": response}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
