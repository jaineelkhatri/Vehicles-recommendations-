from chat_engine import ChatBot

def main():
    bot = ChatBot()
    print("--------------------------------------------------")
    print("Welcome! I am your friendly Python Chatbot.")
    print("Type 'exit' or 'quit' to end the conversation.")
    print("--------------------------------------------------")

    while True:
        try:
            user_input = input("\nYou: ")
            
            if user_input.lower().strip() in ["exit", "quit", "bye"]:
                print(f"Bot: {bot.get_response(user_input)}")
                break
            
            response = bot.get_response(user_input)
            print(f"Bot: {response}")

        except KeyboardInterrupt:
            print("\nBot: Goodbye! Have a great day!")
            break
        except Exception as e:
            print(f"Bot: Oops, something went wrong: {e}")

if __name__ == "__main__":
    main()
