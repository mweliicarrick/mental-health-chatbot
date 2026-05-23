import random

sad_responses = [
    "I'm sorry you're going through that. What do you think has been affecting you the most lately?",

    "That sounds emotionally exhausting. Have you been able to talk to anyone about it?",

    "Sometimes carrying everything alone becomes heavy. What has been on your mind recently?"
]

happy_responses = [
    "That’s really good to hear 😊 What do you think contributed to that positive feeling?",

    "I love hearing that energy from you. What made today better?",

    "That’s beautiful. You should celebrate small wins more often."
]

stress_responses = [
    "Stress can build up quietly sometimes. What has been overwhelming you lately?",

    "You’ve probably been carrying a lot mentally. What usually helps calm you down?",

    "When stress becomes too much, even small things feel heavy. Want to talk about it?"
]

neutral_responses = [
    "Hmm... that's interesting. How did that situation make you feel?",

    "I hear you. What do you think affected you the most there?",

    "That sounds like it stayed on your mind for a while.",

    "What usually goes through your mind when that happens?",

    "I can see why that would affect you.",

    "Was this something recent or has it been building up over time?",

    "That sounds deeper than it looks honestly.",

    "What part of that situation bothered you the most?",

    "Do you feel like people around you understand what you're going through?",

    "How have you been coping with all this mentally?",

    "Sometimes things affect us more quietly than we realize.",

    "What do you wish people understood about how you're feeling?",

    "Has this been affecting your sleep or daily routine too?",

    "Do you feel emotionally drained or just overwhelmed?",

    "That kind of situation can really stay in someone's head.",

    "If you could change one thing about that situation, what would it be?",

    "Do you usually keep these thoughts to yourself?",

    "What helps you feel calm when days become overwhelming?",

    "Would you say this is stressing you emotionally or mentally?",

    "What do you think your mind needs most right now?"
]

advice_list = [
    "Try getting some fresh air today.",

    "Sometimes resting is productive too.",

    "You do not need to solve everything at once.",

    "A small positive routine can slowly change your mindset."
]


def get_response(emotion):
    if emotion == "sad":
        return random.choice(sad_responses)

    elif emotion == "happy":
        return random.choice(happy_responses)

    elif emotion == "stressed":
        return random.choice(stress_responses)

    else:
        return random.choice(neutral_responses)


def get_advice():
    return random.choice(advice_list)