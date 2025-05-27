import random

print("PyBot: Hello! I'm PyBot! Type 'exit' to end the chat.")

responses = {
    "hi": ["Hello there!", "Hi!", "Hey!", "Greetings!"],
    "hello": [
        "Hey! How can I help you today?",
        "Hi! What's up?",
        "Hello! Need something?",
    ],
    "how are you": [
        "I'm just a program, but I'm running great!",
        "All systems operational!",
        "Doing fine, thanks for asking!",
    ],
    "bye": ["Goodbye! Have a nice day!", "Bye! Come back soon!", "Take care!"],
    "who are you": [
        "I'm PyBot, your friendly Python chatbot.",
        "I'm just a little chatbot made in Python.",
    ],
    "help": [
        "You can say hi, ask how I am, or just type something!",
        "Try typing 'hello', 'how are you', or 'bye'!",
    ],
}

while True:
    user_input = input("You: ").lower().strip()

    if user_input == "exit":
        print("PyBot: Chat ended. See you soon!")
        break

    if user_input in responses:
        print("PyBot:", random.choice(responses[user_input]))
