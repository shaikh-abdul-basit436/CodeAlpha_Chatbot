import json
import re
from difflib import SequenceMatcher

KNOWLEDGE_FILE = "app/knowledge/knowledge.json"


def normalize_text(text):
    text = text.lower()
    text = re.sub(r"[^a-z0-9\s]", "", text)
    return " ".join(text.split())


def similarity(text1, text2):
    sequence_score = SequenceMatcher(None, text1, text2).ratio()

    words1 = set(text1.split())
    words2 = set(text2.split())

    if not words1 or not words2:
        token_score = 0
    else:
        token_score = len(words1 & words2) / len(words1 | words2)

    return (sequence_score * 0.6) + (token_score * 0.4)


def load_knowledge():
    with open(KNOWLEDGE_FILE, "r", encoding="utf-8-sig") as file:
        return json.load(file)


def get_response(user_message):
    user_message = normalize_text(user_message)
    knowledge = load_knowledge()

    best_score = 0
    best_response = None

    for intent in knowledge["intents"]:
        for pattern in intent["patterns"]:
            score = similarity(user_message, normalize_text(pattern))

            if score > best_score:
                best_score = score
                best_response = intent["response"]

    if best_score >= 0.40:
        return best_response

    return "I am sorry, I do not have enough information to answer that question."


def chat(user_message):
    if not user_message or not user_message.strip():
        return "Please enter a question."

    return get_response(user_message)
