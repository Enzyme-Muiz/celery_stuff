from celery import Celery
from time import sleep

from celery.schedules import crontab
#from celery.decorators import periodic_task


app = Celery('tasks', broker= 'redis://localhost:6379/0', backend= 'redis://localhost:6379/1')
app.conf.beat_schedule = {
    "trigger-email-notifications": {
        "task": "tasks.every_monday_morning",
        "schedule": 10.0
    }
}
@app.task
def every_monday_morning():
    print("This runs every Monday morning at 7:30a.m.")

#(run_every=crontab(minute="*/2"))
#crontab(minute="*", hour= "*")

@app.task
def reverse(a):
    sleep(10)
    ll= a[::-1]
    return ll



@app.task
def reverse3(a):
    sleep(50)
    ll= a[::-1]
    return ll
 
#celery -A tasks beat --loglevel=info
#celery -A tasks worker -P eventlet --loglevel=info
#reverse3.delay("abcde")
#every_monday_morning.delay()