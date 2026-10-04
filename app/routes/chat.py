from flask import Blueprint, request, jsonify
from app.chatbot.engine import chat

chat_bp = Blueprint("chat", __name__)


@chat_bp.route("/api/chat", methods=["POST"])
def chat_api():
    data = request.get_json(silent=True) or {}
    message = data.get("message", "")

    response = chat(message)

    return jsonify({
        "response": response
    })
