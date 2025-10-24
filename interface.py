# interface.py
from model_loader import load_chat_model
from chat_memory import ChatMemory

def main():
    print("Local Chatbot (type /exit to quit)\n")
    model = load_chat_model()
    memory = ChatMemory(max_turns=3)

    while True:
        user_input = input("You: ")
        if user_input.strip().lower() == "/exit":
            print("Exiting chatbot. Goodbye!")
            break

        # Combine short memory with the new input
        context = memory.get_context()
        prompt = f"{context}\nQuestion: {user_input}\nAnswer:"

        result = model(prompt, max_new_tokens=128)[0]['generated_text']
        print(f"Bot: {result}\n")

        memory.add_turn(user_input, result)

if __name__ == "__main__":
    main()
