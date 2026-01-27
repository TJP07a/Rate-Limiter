from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client["Requests_db"]
requests_collection = db["requests_entries"]