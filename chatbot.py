
from ollama import Client

def main():
        client = Client()
        print(" Your Local Ai Assitant (type 'exit' to quit)")
        while True:
            prompt = input("You: ")
            if prompt.lower() == "exit":
                print("GoodBye!")
                break
            response = client.chat(
                model = "mistral",
                messages=[{"role": "user", "content": prompt}]
            )
            print("AI:", response)
if __name__ == "__main__":
    main()
