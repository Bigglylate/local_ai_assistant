
import sys
import gradio

print("Python executable running script:", sys.executable)
print("Gradio version:", gradio.__version__)
from ollama import Client
import gradio as gr

client = Client()

def chat_with_ai(user_message, chat_history):
    if not user_message:
        return chat_history, "", chat_history

    chat_history = chat_history or []
    chat_history.append({"role": "user", "content": user_message})

    try:
        response = client.chat(
            model="mistral",
            messages=chat_history
        )
        ai_message = response["message"]["content"]
        chat_history.append({"role": "assistant", "content": ai_message})
    except Exception as e:
        chat_history.append({"role": "assistant", "content": f"Error: {str(e)}"})
    return chat_history, "", chat_history


# Set up interface and state
with gr.Blocks() as iface:
    chatbot = gr.Chatbot(type="messages")
    textbox = gr.Textbox(
        placeholder="Type your message...", 
        lines=2,
        submit_btn=True #submit button             
    )
    state = gr.State([])

    textbox.submit(chat_with_ai, inputs=[textbox, state], outputs=[chatbot, textbox, state])

if __name__ == "__main__":
    iface.launch()