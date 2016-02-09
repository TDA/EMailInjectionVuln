__author__ = 'saipc'

from celery import Celery

app = Celery('tasks', broker='amqp://guest@localhost//')

@app.task(name = 'Crawler.celery_test.add')
def add(x, y):
    return x + y
