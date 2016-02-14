__author__ = 'saipc'

from celery import Celery

app = Celery('tasks')
app.conf.update(
    BROKER_URL = 'amqp://guest:guest@localhost:5678//'
)

@app.task(name = 'Crawler.celery_test.add')
def add(x, y):
    return x + y
