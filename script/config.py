import json

def loadJSON(selected_language):
    global MESSAGES

    with open('messages.json', 'r', encoding='utf-8') as f:
        all_messages = json.load(f)

    MESSAGES = all_messages[selected_language]
    return MESSAGES


MESSAGES = loadJSON("de") # SPRACHE NOCH ÄNDERN
