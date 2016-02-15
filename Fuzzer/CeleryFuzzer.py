from __future__ import absolute_import

from celery import Celery

__author__ = 'saipc'

app = Celery('CeleryFuzzer',
             backend='amqp://',
             include=['Fuzzer.call_email_form_retriever', 'Fuzzer.email_form_retriever', 'Fuzzer.fuzzer'])

# Optional configuration, see the application user guide.
app.conf.update(
    CELERY_TASK_RESULT_EXPIRES=3600,
    BROKER_URL = 'amqp://guest:guest@localhost:5679//'
)

if __name__ == '__main__':
    app.start()
