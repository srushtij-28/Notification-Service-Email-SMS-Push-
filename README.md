# Notification Service

A Flask microservice for sending Email, SMS, and Push notifications asynchronously.

## Features

- Email notifications
- SMS notifications
- Push notifications
- Celery background processing
- Redis message broker

## Technologies Used

- Python
- Flask
- Celery
- Redis

## Installation

```bash
pip install -r requirements.txt
```

Start Redis
docker compose up -d

Start Celery Worker
celery -A tasks worker --loglevel=info

Run Flask
python app.py
