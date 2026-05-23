from emotions import detect_emotion
from therapist_ai import get_response, get_advice
from crisis_support import detect_crisis
from memory import add_to_memory
from datetime import datetime

def save_chat(user, bot):
    with open("chat_logs.txt", "a", encoding="utf-8") as file:
        file.write(f"\n[{datetime.now()}]\n")
        file.write(f"User: {user}\n")
        file.write(f"Bot: {bot}\n")

def generate_response(user_input):

    add_to_memory(user_input)

    if detect_crisis(user_input):
        response = (
            "⚠️ I'm really concerned about what you're saying.\n\n"
            "Please reach out to someone you trust or a mental health professional.\n"
            "You matter more than you think."
        )

        save_chat(user_input, response)
        return response

    emotion = detect_emotion(user_input)

    response = get_response(emotion)

    # Occasionally add advice
    import random

    if random.randint(1, 3) == 1:
        response += "\n\n💡 Advice: " + get_advice()

    save_chat(user_input, response)

    return response