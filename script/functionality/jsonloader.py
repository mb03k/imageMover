import json

def loadJSON(selected_language):
    with open('messages.json', 'r', encoding='utf-8') as f:
        all_messages = json.load(f)

    MESSAGES = all_messages[selected_language]
    return MESSAGES