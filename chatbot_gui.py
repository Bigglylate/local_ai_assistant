
from ollama import Client
import gradio as gr

client = Client()

def chat_with_ai(prompt):
    if not prompt:
        return "Please enter a message"
    response = client.chat(
        model = "mistral",
        messages=[{"role": "user", "content": prompt}]
        )
    return response["message"]["content"]

iface = gr.Interface(
    fn = chat_with_ai,
    inputs=gr.Textbox(lines=5, placeholder= "Type your message here...."),
    outputs="text",
    title = "Local AI CHATBOT",
    description= "Chat with your local AI powered by Ollama's Mistral model."
    
    
    
)

if __name__ == "__main__":
    iface.launch()