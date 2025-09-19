# local_ai_assistant
learning how to create a local ai assistant using Python

A local AI assistant chatbot application built with React(Frontend) and FastAPI(Backend),
integrated with Ollama for AI reponses.

Features:

- Interactive chat interface
- FastAPI backend with "/chat endpoint" and "/health" endpoint
- Local Ai processing via Ollama
- Logs all user and bot messages
- Modular structure for future improvements

Requirements:

- Python 3.8+
- Node.js 14+
- Ollama installed and acessible in your PATH
- Windows recommended for the ".bat" file

Inastallation and Setup:

1. Clone the repository:
   git clone

2. Backend Setup:
   cd local_ai_assistant/backend
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   pip install -r requirements.txt
   uvicorn main:app --reload

3. Frontend Setup:
   cd ../frontend
   npm install
   npm start

Running the Applicaition:

You can start both the frontend and backend with the batch file

This will:

1. Open a terminal and start the FastAPI backend server.
1. Open another terminal and start the React frontend development server.

License
MIT liecne - feel free to modify and use as needed.