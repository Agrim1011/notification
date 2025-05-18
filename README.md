# 📨 Notification Service – Backend Intern Assignment

A FastAPI-based backend service for sending notifications via Email, SMS, and In-App channels using asynchronous message queues and MongoDB storage.

---

## 🚀 Features

- ✅ Send notifications via REST API (`POST /notifications`)
- ✅ Retrieve all notifications for a user (`GET /users/{id}/notifications`)
- ✅ Supports Email, SMS, and In-App channels
- ✅ Asynchronous processing using RabbitMQ
- ✅ Stores In-App notifications in MongoDB
- ✅ Modular, scalable, and ready for production extension

---

## 🧱 Tech Stack

- **Backend Framework:** FastAPI  
- **Database:** MongoDB  
- **Queue System:** RabbitMQ  
- **Queue Handler:** Pika (Python)  
- **Others:** Postman, Docker (for RabbitMQ), Python 3.10+

---

## 🧪 Running the App Locally

1. Clone the repo:
    ```bash
    git clone https://github.com/Agrim1011/notification.git
    cd notification
    ```
2. Create and activate virtual environment:
    ```bash
    python -m venv env
    source env/bin/activate  # On Windows: .\env\Scripts\activate
    ```
3. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```
4. Run MongoDB locally or use MongoDB Atlas.
5. Start FastAPI server:
    ```bash
    uvicorn main:app --reload
    ```
6. Run the consumer in another terminal:
    ```bash
    python consumer.py
    ```

---

✨ **Author**  
Agrim Goyal  
[LinkedIn](https://linkedin.com/in/agrim1011) | [GitHub](https://github.com/Agrim1011)
