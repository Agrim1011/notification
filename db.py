from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017")
db = client.notification_db
collection = db.notifications

def save_notification(data):
    collection.insert_one(data)

def get_notifications_for_user(user_id):
    return list(collection.find({"user_id": user_id}, {"_id": 0}))
