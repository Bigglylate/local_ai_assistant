
import sys
import gradio

print("Python executable running script:", sys.executable)
print("Gradio version:", gradio.__version__)
from chatbot import get_ai_response
import gradio as gr

chat_history = []

def chat_interface(user_message):
    global chat_history
    chat_history = get_ai_response(user_message, chat_history)

    # Format for display in Gradio
    formatted = ""
    for msg in chat_history:
        role = msg["role"].capitalize()
        formatted += f"{role}: {msg['content']}\n\n"
    return formatted, ""

def clear_chat():
    """
        Clears the chat history and UI

    """

    global chat_history
    chat_history = []
    return "", "" # Clear the chat history and UI


# Build the Gradio interface
with gr.Blocks() as iface:

    gr.Markdown("# AI Chatbot")
    gr.Markdown("Press Enter to send, Shift+Enter for a new line")

    chatbot_box = gr.Textbox(lines=20, 
                             label="Conversation", 
                             interactive=False,
                             elem_id = "chat_display")

    user_input = gr.Textbox(lines = 2, 
                            placeholder="Type your message here...",)

    send_btn = gr.Button("Send")
    clear_btn = gr.Button("Clear Chat")

    # Bind Enter (submit) to chat function
    user_input.submit(chat_interface, inputs=user_input, outputs=[chatbot_box, user_input])


    # Buttons
    send_btn.click(chat_interface, inputs=user_input, outputs=[chatbot_box, user_input])
    clear_btn.click(clear_chat, inputs=None, outputs=[chatbot_box, user_input])

if __name__ == "__main__":
    iface.launch(inbrowser=True)