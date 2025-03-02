# ──────────────────────────────────────────────────────────────────────────────────────────────
# Generic Open AI chatbot
# ──────────────────────────────────────────────────────────────────────────────────────────────

# Import necessary packages
import openai
from dotenv import load_dotenv
import os

# Load key from env file
load_dotenv(
    "/Users/abhisheksingh/VS_Code_Projects/analytics/analytics/analytics/chatbot/chatbot.env"
)

client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))  # Create client instance


def chat_with_gpt(prompt):
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}],
    )
    return response.choices[0].message.content.strip()


if __name__ == "__main__":
    while True:
        user_input = input("You: ")
        if user_input.lower() in [
            "quit",
            "exit",
            "bye",
        ]:  # Fixing `.lower` method usage
            break

        response = chat_with_gpt(user_input)
        print("Chatbot:", response)
