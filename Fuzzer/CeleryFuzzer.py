from __future__ import absolute_import

from celery import Celery

__author__ = 'saipc'

app = Celery('CeleryFuzzer',
             broker='amqp://',
             backend='amqp://',
             include=['Fuzzer.email_form_retriever'])

# Optional configuration, see the application user guide.
app.conf.update(
    CELERY_TASK_RESULT_EXPIRES=3600,
)

if __name__ == '__main__':
    app.start()
