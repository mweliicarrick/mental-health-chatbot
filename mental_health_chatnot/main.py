import tkinter as tk
from tkinter import scrolledtext
from chatbot_engine import generate_response

# Window
root = tk.Tk()
root.title("MindEase AI")
root.geometry("800x650")
root.config(bg="#0f0f0f")

# Colors
BG = "#0f0f0f"
CHAT_BG = "#1a1a1a"
USER_BG = "#00ff99"
BOT_BG = "#262626"
TEXT = "#ffffff"

# Header
header = tk.Label(
    root,
    text="🧠 MindEase AI Therapist",
    bg=BG,
    fg="#00ff99",
    font=("Helvetica", 20, "bold")
)

header.pack(pady=10)

# Chat area
chat_area = scrolledtext.ScrolledText(
    root,
    wrap=tk.WORD,
    bg=CHAT_BG,
    fg=TEXT,
    font=("Segoe UI Emoji", 12),
    bd=0
)

chat_area.pack(padx=15, pady=10, fill=tk.BOTH, expand=True)
chat_area.config(state="disabled")

# Input frame
input_frame = tk.Frame(root, bg=BG)
input_frame.pack(fill=tk.X, padx=15, pady=10)

# User entry
user_input = tk.Entry(
    input_frame,
    bg="#1f1f1f",
    fg="white",
    insertbackground="white",
    font=("Segoe UI Emoji", 12),
    relief=tk.FLAT
)

user_input.pack(side=tk.LEFT, fill=tk.X, expand=True, ipady=10)

# Add message
def add_message(sender, message, tag):

    chat_area.config(state="normal")

    chat_area.insert(tk.END, f"{sender}: {message}\n\n", tag)

    chat_area.tag_config(
        "user",
        foreground="#00ff99"
    )

    chat_area.tag_config(
        "bot",
        foreground="#ffffff"
    )

    chat_area.config(state="disabled")
    chat_area.yview(tk.END)

# Send message
def send_message():

    message = user_input.get()

    if not message.strip():
        return

    add_message("You", message, "user")

    response = generate_response(message)

    add_message("MindEase", response, "bot")

    user_input.delete(0, tk.END)

# Enter key
user_input.bind("<Return>", lambda event: send_message())

# Send button
send_button = tk.Button(
    input_frame,
    text="Send",
    command=send_message,
    bg="#00ff99",
    fg="black",
    font=("Segoe UI Emoji", 11, "bold"),
    relief=tk.FLAT,
    padx=20
)

send_button.pack(side=tk.LEFT, padx=10)

# Welcome
add_message(
    "MindEase",
    "Hello 😊 I'm here for you.\nHow has your mind been feeling lately?",
    "bot"
)

root.mainloop()