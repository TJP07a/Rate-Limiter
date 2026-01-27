from flask import Flask, jsonify
from db import requests_collection
from routes.route import register_routes

app = Flask(__name__)

register_routes(app)

@app.route("/health", methods=["GET"])
def get_health():
    return jsonify({"message": "Health, ok"}), 200

if __name__ == "__main__":
    app.run(debug=True)