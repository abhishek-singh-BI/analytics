# Chatbot Project

This project implements an AI-powered chatbot that interacts with users, handles specific topics, and provides responses using OpenAI's GPT-3.5 model. The backend is built using FastAPI, and the frontend is built with Streamlit.

## Project Structure

The directory structure of the project is as follows:

        ├── chatbot
        │   ├── LICENSE
        │   ├── README.MD
        │   ├── chatbot.env
        │   └── src
        │       ├── __pycache__
        │       │   └── chatbot.cpython-312.pyc
        │       ├── chatbot.py
        │       └── streamlit_front_end.py


## Prerequisites

Before you run the project, make sure you have the following:

- Python 3.8 or higher
- OpenAI API Key
- FastAPI
- Streamlit

### Installing Dependencies

To set up the project, you'll need to install the required dependencies. It's recommended to use a virtual environment for managing the dependencies.

1. **Create a virtual environment:**

        python -m venv .venv


2. **Activate the virtual environment:**

- For macOS/Linux:
  ```
  source .venv/bin/activate
  ```

- For Windows:
  ```
  .venv\Scripts\activate
  ```

3. **Install dependencies:**

    Install the required Python libraries by running:

        pip install -r requirements.txt


    Where `requirements.txt` should contain the following:

        openai fastapi requests pydantic uvicorn streamlit python-dotenv


## Setup Environment Variables

Create a `.env` file in the root of the `chatbot` directory and add your OpenAI API key as follows:

        OPENAI_API_KEY=your_openai_api_key_here


Replace `your_openai_api_key_here` with your actual OpenAI API key.

## Running the Application

1. **Start the FastAPI backend server:**

   Navigate to the `src` folder and run the FastAPI application:

        uvicorn chatbot:app --reload


    This will start the FastAPI server at `http://127.0.0.1:8000`.

2. **Start the Streamlit frontend:**

    In another terminal window, run the Streamlit frontend by executing:

        streamlit run src/streamlit_front_end.py


    This will open a browser window or provide a URL where you can interact with the chatbot.

## How It Works

1. The user enters a question in the Streamlit frontend.
2. The question is sent to the FastAPI backend (`/chat` endpoint).
3. The backend uses the OpenAI API to generate a response based on the user’s input.
4. If the user’s message contains restricted topics such as pricing, policy, or confidential matters, the response will guide the user to contact support.
5. The generated response is sent back to the frontend, which displays it to the user.

## Restricted Topics

The backend restricts certain topics for responses. These include:

- **pricing**
- **policy**
- **confidential**

For any questions related to these topics, users are directed to contact support.

## Error Handling

- If the user exceeds the available quota for the OpenAI API, the response will notify them of the quota limit.
- If an error occurs on the backend, a generic error message will be returned to the user.

## Project Future Enhancements

- **Multilingual Support**: Add the ability to respond in multiple languages.
- **User Authentication**: Implement user authentication to personalize the chat experience.
- **Database Integration**: Save chat history for users and make it accessible in future sessions.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contact

For support, please reach out to [abhi_07786@yahoo.in]




