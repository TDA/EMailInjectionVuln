from __future__ import absolute_import

from celery import Celery

__author__ = 'saipc'

app = Celery('CeleryFuzzer',
             backend='amqp://',
             include=['call_email_form_retriever', 'email_form_retriever', 'fuzzer'])

# Optional configuration, see the application user guide.
app.conf.update(
    CELERY_TASK_RESULT_EXPIRES=3600,
    BROKER_URL = 'amqp://guest:guest@localhost:5678//',
    CELERY_IGNORE_RESULT = True,
    CELERY_ROUTES = {'Fuzzer.call_email_form_retriever': {'queue': 'fuzzing'},
                     'Fuzzer.call_fuzzer_with_payload': {'queue': 'fuzzing'},
                     # 'Fuzzer.parse_email': {'queue': 'fuzzing'},
                     'Fuzzer.call_fuzzer_with_malicious_payload': {'queue': 'fuzzing'},
                     'Fuzzer.email_form_retriever': {'queue': 'fuzzing'},
                     'Fuzzer.fuzzer': {'queue': 'fuzzing'},
                     }
)

if __name__ == '__main__':
    app.start()
