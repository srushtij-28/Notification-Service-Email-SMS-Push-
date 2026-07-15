from celery import Celery
import time

celery = Celery(
    "tasks",
    broker="redis://localhost:6379/0",
    backend="redis://localhost:6379/0"
)

@celery.task
def send_email(email, subject):

    time.sleep(2)

    return f"Email sent to {email}"

@celery.task
def send_sms(number):

    time.sleep(2)

    return f"SMS sent to {number}"

@celery.task
def send_push(user):

    time.sleep(2)

    return f"Push notification sent to {user}"
