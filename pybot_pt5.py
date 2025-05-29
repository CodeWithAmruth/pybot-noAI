import random
from datetime import datetime

print("PyBot: Hello! I'm PyBot! Type 'exit' to end the chat.")

responses = {
    ("hi", "hello", "hey"): ["Hey there!", "Hi!", "Hello!", "What's up?"],
    ("how are you", "how are things", "how’s it going"): [
        "I'm running smoothly, thanks!",
        "All systems go!",
        "Doing great!",
    ],
    ("bye", "goodbye", "see you"): ["See you later!", "Goodbye!", "Take care!"],
    ("who are you", "what are you", "what is your name"): [
        "I'm PyBot, your Python-powered chat companion."
    ],
    ("what do you do", "why were you built", "what is your purpose"): [
        "I'm here to chat and help you learn Python basics!"
    ],
    ("help", "commands", "options"): [
        "You can say hi, ask who I am, or just type something!"
    ],
}

log_file = "chat_log_pt5.txt"

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

    found = False
    for keys, replies in responses.items():
        if user_input in keys:
            bot_reply = random.choice(replies)
            found = True
            break

    if not found:
        bot_reply = "I'm not sure how to respond to that."

    print("PyBot:", bot_reply)

    with open(log_file, "a") as log:
        log.write("You: {}\n".format(user_input))
        log.write("PyBot: {}\n".format(bot_reply))
