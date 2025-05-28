import random
from datetime import datetime

print("PyBot: Hello! I'm PyBot! Type 'exit' to end the chat.")

responses = {
    "hi": ["Hello there!", "Hi!", "Hey!", "Greetings!"],
    "hello": [
        "Hey! How can I help you today?",
        "Hi there! What's up?",
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

# Log file setup
log_file = "chat_log.txt"

with open(log_file, "a") as log:
    log.write(
        "\n=== New Chat Started at {} ===\n".format(
            datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        )
    )

while True:
    user_input = input("You: ").lower().strip()

    if user_input == "exit":
        print("PyBot: Chat ended. See you soon!")
        with open(log_file, "a") as log:
            log.write("You: {}\n".format(user_input))
            log.write("PyBot: Chat ended. See you soon!\n")
        break

    if user_input in responses:
        bot_reply = random.choice(responses[user_input])
    else:
        bot_reply = "I'm not sure how to respond to that."

    print("PyBot:", bot_reply)

    # Log user and bot messages
    with open(log_file, "a") as log:
        log.write("You: {}\n".format(user_input))
        log.write("PyBot: {}\n".format(bot_reply))
