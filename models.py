from pydantic import BaseModel

class NotificationRequest(BaseModel):
    user_id: str
    message: str
    type: str  # "email", "sms", "inapp"
