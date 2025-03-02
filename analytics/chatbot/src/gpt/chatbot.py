import openai
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from dotenv import load_dotenv
import os

# Initialize FastAPI app
app = FastAPI()

# Load environment variables from the .env file
load_dotenv(
    "/Users/abhisheksingh/VS_Code_Projects/analytics/analytics/analytics/chatbot/chatbot.env"
)

# Get the OpenAI API key from the environment
openai.api_key = os.getenv("OPENAI_API_KEY")

# Check if the API key is loaded
if openai.api_key is None:
    raise ValueError(
        "API key not found. Please set the OPENAI_API_KEY in the .env file."
    )

# Restricted topics
RESTRICTED_TOPICS = ["pricing", "policy", "confidential"]
SUPPORT_EMAIL = "support@example.com"


# Request model
class ChatRequest(BaseModel):
    message: str


# Function to get response from OpenAI using the new method
def get_openai_response(user_input: str) -> str:
    if any(topic in user_input.lower() for topic in RESTRICTED_TOPICS):
        return f"Please reach out to {SUPPORT_EMAIL} for more details."

    try:
        # This should work with openai.Completion.create in openai version >= 1.0.0
        response = openai.completions.create(
            model="gpt-3.5-turbo",  # Make sure to use a valid model like gpt-3.5-turbo
            prompt=user_input,  # Provide the prompt (this is the user's input)
            temperature=0.7,  # Adjust the temperature based on how creative the response should be
            max_tokens=150,  # Optional: Limit the length of the response
        )

        return response["choices"][0]["text"]  # Extract the response text
    except Exception as e:
        print(f"Error occurred: {e}")  # Detailed error log
        return f"Sorry, I am unable to process the request right now. Error: {str(e)}"


# API endpoint to process user requests
@app.post("/chat")
def chat(request: ChatRequest):
    try:
        response = get_openai_response(request.message)
        return {"response": response}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
