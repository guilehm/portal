import django
django.setup()

from django.utils import timezone
from apscheduler.schedulers.background import BackgroundScheduler
from register.models import Message


scheduler = BackgroundScheduler()


@scheduler.scheduled_job('interval', minutes=1)
def create_message():
    message = Message(message=str(timezone.now()))
    message.save()


scheduler.start()

while True:
    pass
