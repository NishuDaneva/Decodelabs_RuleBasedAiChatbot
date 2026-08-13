print("========================================")
print("      RULE-BASED AI CHATBOT")
print("========================================")
print("Type 'help' to see available commands.")
print("Type 'bye' to exit.\n")

while True:
    user = input("You: ").strip().lower()

    if user == "hello":
        print("Bot: Hello! How can I help you?")

    elif user == "hi":
        print("Bot: Hi! Nice to meet you.")

    elif user == "how are you":
        print("Bot: I'm doing great. Thanks for asking!")

    elif user == "your name":
        print("Bot: My name is Rule-Based AI Chatbot.")

    elif user == "help":
        print("Bot: You can say: hello, hi, how are you, your name, thanks, bye")

    elif user == "thanks":
        print("Bot: You're welcome!")

    elif user == "bye":
        print("Bot: Goodbye! Have a nice day.")
        break

    else:
        print("Bot: Sorry, I don't understand. Please try another question.")