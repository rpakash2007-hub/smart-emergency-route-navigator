from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")

db = client["emergency_route_navigator"]

emergency_collection = db["emergency_requests"]

print("MongoDB connection setup ready!")