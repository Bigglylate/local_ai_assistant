import subprocess

def query_ollama(prompt: str, model: str = "mistral") -> str:
    """

    Send a prompt to the Ollama model and return the response.

    """

    result = subprocess.run(
        ["ollama", "query", model, prompt],
        capture_output=True,
        text=True,
    )

    return result.stdout.strip()
