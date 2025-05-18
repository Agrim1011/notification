def send_email(data):
    print(f"Sending EMAIL to {data['user_id']}: {data['message']}")

def send_sms(data):
    print(f"Sending SMS to {data['user_id']}: {data['message']}")
