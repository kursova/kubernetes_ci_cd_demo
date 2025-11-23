# main.py
from flask import Flask, jsonify
import os

def create_app():
    app = Flask(__name__)

    @app.route("/")
    def hello():
        env = os.getenv("APP_ENV", "dev")
        return f"Hello from {env} environment!"

    @app.route("/health")
    def health():
        return jsonify(status="ok"), 200

    return app

app = create_app()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)