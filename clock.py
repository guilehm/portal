import django  # noqa
django.setup()

from apscheduler.schedulers.background import BackgroundScheduler

from register.models import Message


scheduler = BackgroundScheduler()


@scheduler.scheduled_job('interval', minutes=2)
def create_message():
    message = Message(message='teste')
    message.save()


scheduler.start()

while True:
    pass
