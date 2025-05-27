print("Bot: Hi,I'm a PyBot! Type 'bye' to exit.")


while True:
    user = input("You: ").lower()

    if user == "hello":
        print("Bot: Hello!")
    elif user == "how are you?":
        print("Bot: I'm fine, thank you.")
    elif user == "what is your name?":
        print("Bot: My name is PyBot.")
    elif user == "bye":
        print("Bot: Bye!")
        break
    else:
        print("Bot:Sorry, I don't understand.")
