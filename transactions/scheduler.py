from apscheduler.schedulers.background import BackgroundScheduler
from model_mommy import mommy

from register.models import Message

scheduler = BackgroundScheduler()


@scheduler.scheduled_job('interval', minutes=2)
def create_message():
    return mommy.make(Message)


scheduler.start()
