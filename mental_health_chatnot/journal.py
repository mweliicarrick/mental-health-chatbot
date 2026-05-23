import random

prompts = [
    "What made you smile today?",
    "What are you grateful for today?",
    "Describe how you are feeling right now.",
    "What is one thing you wish to improve?",
    "What motivates you to keep going?"
]

def get_journal_prompt():
    return random.choice(prompts)