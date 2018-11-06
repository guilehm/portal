import django
from apscheduler.schedulers.background import BackgroundScheduler

from register.models import Message

django.setup()

scheduler = BackgroundScheduler()


@scheduler.scheduled_job('interval', minutes=2)
def create_message():
    message = Message(message='teste')
    message.save()


scheduler.start()

while True:
    pass
