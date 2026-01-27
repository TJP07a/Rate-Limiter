from flask import Flask, jsonify, request
# from db import requests_collection
import secrets
import hashlib

def generate_api():
    return secrets.token_urlsafe(32)

def hash_api_key(api_key):
    return hashlib.sha256(api_key.encode()).hexdigest()

# server generates and stores ONE valid API key
_RAW_API_KEY = generate_api()
VALID_API_KEY = hash_api_key(_RAW_API_KEY)

print("VALID API KEY (copy this for test.py):", VALID_API_KEY)

def register_routes(app):
    @app.route("/request-health-status", methods = ["GET"])
    def request_health_status():
        api_key = request.headers.get("X-API-KEY")
    
        if not api_key:
            return jsonify({"error": "No API Key"}), 401
    
        if not api_key == VALID_API_KEY:
            return jsonify({"error": "API Key mismatch"}), 403

        
        print("Request received")
        return jsonify({"message": "Health is ok"}), 200
    
    @app.route("/request-api-key", methods=["GET"])
    def get_api_key():
        return jsonify({
            "api_key": VALID_API_KEY
        }), 200