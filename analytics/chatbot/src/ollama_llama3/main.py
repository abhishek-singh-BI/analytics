# Import the model
from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate

# Template for the model to tell it, how to behave and respond
template = """
Answer the question below.

Here is the conversation history: {context}

Question: {question}

Answer:
"""

# Specify the model you want to work with
model = OllamaLLM(model="llama3")

# Specify the prompt using the template defined above
prompt = ChatPromptTemplate.from_template(template)

# Chain the prompt and model together. First prompt is called and then using prompt model is invoked
chain = prompt | model


# Function to handle the conversation
def handle_conversation():
    context = ""
    print("Welcome to AI ChatBot, Type 'exit' to quit")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            break
        result = chain.invoke({"context": context, "question": user_input})
        print("Bot: ", result)
        # Pass the context after the first chat
        context += f"\nUser: {user_input}\nAI: {result}"


# Call the handle conversation chatbot main code
if __name__ == "__main__":
    handle_conversation()
