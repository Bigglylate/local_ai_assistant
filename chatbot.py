"""
    
 This module contains all AI logic for the chatbot application.
 It handes communcting with Ollama and managing chat history.

"""
from pyexpat import model
from ollama import Client

#initialize Ollama client
client = Client()

def get_ai_response(user_message, chat_history):
    """
    Sends user message and chat_history to Ollama client and
    returns updated chat history with AI response.

    """

    chat_history = chat_history or []

    chat_history.append({"role": "user", "content": user_message})

    try:

        # Ask AI for response

        response = client.chat(
            model="mistral", # Replace with your ollama model name
            messages=chat_history
        )
        ai_message = response["message"]["content"]
        chat_history.append({"role": "assistant", "content": ai_message})
    except Exception as e:
            chat_history.append({"role": "assistant", "content": f"Error: {str(e)}"})

    return chat_history
