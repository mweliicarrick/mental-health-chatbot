from textblob import TextBlob

def detect_emotion(text):
    text = text.lower()

    if any(word in text for word in [
        "stress", "tired", "overwhelmed", "pressure"
    ]):
        return "stressed"

    analysis = TextBlob(text)
    polarity = analysis.sentiment.polarity

    if polarity > 0.3:
        return "happy"

    elif polarity < -0.3:
        return "sad"

    else:
        return "neutral"