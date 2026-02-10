from pymongo import MongoClient

client = MongoClient("mongodb://localhost:0000/")
db = client["Requests_db"]
requests_collection = db["requests_entries"]
