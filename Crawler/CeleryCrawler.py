from __future__ import absolute_import

from celery import Celery

app = Celery('CeleryCrawler',
             backend='amqp://',
             include=['form_parser', 'check_for_email', 'call_form_parser', 'call_check_for_email'])

# Optional configuration, see the application user guide.
app.conf.update(
    CELERY_TASK_RESULT_EXPIRES=3600,
    BROKER_URL = 'amqp://guest:guest@localhost:5678//'
)

if __name__ == '__main__':
    app.start()
