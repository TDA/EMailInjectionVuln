__author__ = 'saipc'

from CeleryCrawler import Celery

app = Celery('tasks', broker='amqp://guest@localhost//')

@app.task
def add(x, y):
    return x + y