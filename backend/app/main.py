
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import subprocess

# ----------------------------------
# FastAPI app setup
#----------------------------------



app = FastAPI()

app.add_middleware(
	CORSMiddleware,
	allow_origins=["http://localhost:5173"],
	allow_credentials=True,
	allow_methods=["*"],
	allow_headers=["*"],
)
#----------------------------------
#Request and Response Models
#----------------------------------


class ChatRequest(BaseModel):
	prompt: str

class ChatResponse(BaseModel):
	response: str


#----------------------------------
# Health check
#----------------------------------

@app.get("/health")
def health_check():
	return {"status": "ok"}

#----------------------------------
# Chatbot endpoint
#----------------------------------

@app.post("/chat", response_model=ChatResponse)
def chat_endpoint(request: ChatRequest):
	try:
		# Run the Ollama command to get the response
		result = subprocess.run(
			["ollama", "run", "mistral", request.prompt],
			capture_output=True,
			text=True,
		)
		if result.returncode != 0:
			return ChatResponse(response="Error: Unable to get response from model.")

		return ChatResponse(response=result.stdout.strip())
	except Exception as e:
		return ChatResponse(response=f"Error: {str(e)}")
	


