crisis_keywords = [
    "suicide",
    "kill myself",
    "self harm",
    "depressed",
    "hopeless",
    "die",
    "death",
    "murder"
]

def detect_crisis(text):
    text = text.lower()

    for word in crisis_keywords:
        if word in text:
            return True

    return False