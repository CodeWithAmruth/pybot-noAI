print("PyBot: Hello! I'm PyBot!. Type 'exit' to end the chat.")

responses = {
    "hi": "Hello there!",
    "hello": "Hey! How can I help you today?",
    "how are you": "I'm just a program, but I'm running great!",
    "bye": "Goodbye! Have a nice day!",
    "who are you": "I'm PyBot, your friendly Python chatbot.",
    "help": "You can say hi, ask how I am, or just type something!",
}

while True:
    user_input = input("You: ").lower().strip()

    if user_input == "exit":
        print("PyBot: Chat ended. See you soon!")
        break

    reply = responses.get(user_input, "I'm not sure how to respond to that.")
    print("PyBot:", reply)