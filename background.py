import django
django.setup()

from apscheduler.schedulers.background import BackgroundScheduler


scheduler = BackgroundScheduler()


@scheduler.scheduled_job('interval', minutes=1)
def do_something():
    pass  # do something here


scheduler.start()

while True:
    pass
