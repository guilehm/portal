from apscheduler.schedulers.background import BackgroundScheduler
from model_mommy import mommy

scheduler = BackgroundScheduler()


@scheduler.scheduled_job('interval', minutes=2)
def create_message():
    return mommy.make('register.Message')


scheduler.start()
