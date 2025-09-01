# Allow running scripts

Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass 

# Activate virtual Enviroment
.\venv\Scripts\activate

# Run the assistant script
python .\chatbot_gui.py

# Keep window open to see any messages

pause