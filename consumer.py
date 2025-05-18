import pika, json
from db import save_notification
from utils import send_email, send_sms

def callback(ch, method, properties, body):
    data = json.loads(body)
    print(f"Processing: {data}")
    try:
        if data["type"] == "email":
            send_email(data)
        elif data["type"] == "sms":
            send_sms(data)
        elif data["type"] == "inapp":
            save_notification(data)
    except Exception as e:
        print("Error:", e)

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()
channel.queue_declare(queue='notifications')
channel.basic_consume(queue='notifications', on_message_callback=callback, auto_ack=True)
print("Waiting for messages...")
channel.start_consuming()
