from fastapi import FastAPI
from models import NotificationRequest
from producer import publish_to_queue
from db import get_notifications_for_user

app = FastAPI()

@app.post("/notifications")
async def send_notification(request: NotificationRequest):
    publish_to_queue(request.dict())
    return {"status": "queued"}

@app.get("/users/{user_id}/notifications")
async def get_user_notifications(user_id: str):
    return get_notifications_for_user(user_id)
