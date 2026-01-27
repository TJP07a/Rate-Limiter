import requests

def get_api_key():
    response = requests.get("http://127.0.0.1:5000/request-api-key")
    return response.json()["api_key"]

def send_request():
    API_KEY = get_api_key()
    response = requests.get("http://127.0.0.1:5000/request-health-status",
                        headers= {"X-API-KEY": API_KEY}
                        )
send_request()