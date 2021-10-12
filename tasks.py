from celery import Celery
from time import sleep
app = Celery('tasks', broker= 'redis://localhost:6379/0', backend= 'redis://localhost:6379/1')
@app.task
def reverse(a):
    sleep(10)
    ll= a[::-1]
    return ll
 