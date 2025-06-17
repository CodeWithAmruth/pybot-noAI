import tkinter as tk
import random
from datetime import datetime

# --- Chatbot logic ---

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

log_file = "chat_log_gui.txt"

with open(log_file, "a") as log:
    log.write(
        "\n=== New GUI Chat Started at {} ===\n".format(
            datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        )
    )


# --- Function to handle sending messages ---


def send_message():
    user_input = entry.get().lower().strip()
    if not user_input:
        return

    chat_log.insert(tk.END, "You: " + user_input + "\n")
    entry.delete(0, tk.END)

    if user_input == "exit":
        bot_reply = "Chat ended. See you soon!"
        chat_log.insert(tk.END, "PyBot: " + bot_reply + "\n")
        save_log(user_input, bot_reply)
        root.quit()
        return

    found = False
    for keys, replies in responses.items():
        if user_input in keys:
            bot_reply = random.choice(replies)
            found = True
            break

    if not found:
        bot_reply = "I'm not sure how to respond to that."

    chat_log.insert(tk.END, "PyBot: " + bot_reply + "\n")
    save_log(user_input, bot_reply)


# --- Function to log chat ---


def save_log(user, bot):
    with open(log_file, "a") as log:
        log.write("You: {}\n".format(user))
        log.write("PyBot: {}\n".format(bot))


# --- GUI Setup ---

root = tk.Tk()
root.title("PyBot Chatbot")
root.geometry("500x500")

chat_log = tk.Text(root, bd=1, bg="black", fg="lime", font=("Courier", 12))
chat_log.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

entry = tk.Entry(root, bd=1, font=("Courier", 12))
entry.pack(padx=10, pady=(0, 10), fill=tk.X)
entry.bind("<Return>", lambda event: send_message())

send_button = tk.Button(root, text="Send", command=send_message)
send_button.pack(pady=(0, 10))

chat_log.insert(tk.END, "PyBot: Hello! I'm PyBot! Type 'exit' to end the chat.\n")

root.mainloop()
