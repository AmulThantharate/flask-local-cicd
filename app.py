import os
from flask import Flask, jsonify

app = Flask(__name__)

APP_ENV = os.getenv("APP_ENV", "dev")
DEBUG = os.getenv("APP_DEBUG", "false").lower() == "true"


@app.route("/")
@app.route("/health")
def health():
    return jsonify({"status": "ok", "environment": os.getenv("APP_ENV", "dev")})


if __name__ == "__main__":
    app.run(debug=DEBUG, host="0.0.0.0", port=8080)
