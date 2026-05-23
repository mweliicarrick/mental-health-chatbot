conversation_memory = []

def add_to_memory(message):
    conversation_memory.append(message)

    if len(conversation_memory) > 10:
        conversation_memory.pop(0)

def get_memory():
    return conversation_memory