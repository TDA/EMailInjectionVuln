from __future__ import absolute_import

from celery import Celery

app = Celery('Crawler',
             broker='amqp://',
             backend='amqp://',
             include=['Crawler.form_parser', 'Crawler.check_for_email'])

# Optional configuration, see the application user guide.
app.conf.update(
    CELERY_TASK_RESULT_EXPIRES=3600,
)

if __name__ == '__main__':
    app.start()
