from flask import Flask, send_from_directory
from flask_cors import CORS
from app.routes.chat import chat_bp

app = Flask(__name__, static_folder="../frontend", static_url_path="")
CORS(app)

app.register_blueprint(chat_bp)


@app.route("/")
def index():
    return send_from_directory("../frontend", "index.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
