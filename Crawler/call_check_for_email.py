from __future__ import absolute_import
from celery import Celery
from CeleryCrawler import app

from functions import *
from check_for_email import check_for_email_field




# open a db connection and retrieve all the forms that need to be checked
# if they actually contain email fields, this starts up a celery
# concurrent program
@app.task(name='Crawler.call_check_for_email')
def call_check_for_email():
    db = getopenconnection()
    cursor = db.cursor()
    select_query = "SELECT id,xpath from form"
    # only these two fields are required
    cursor.execute(select_query)
    rows = cursor.fetchall()
    tasks = []
    for row in rows:
        tasks.append(check_for_email_field.delay(row))

    # no of rows retrieved basically
    print(len(tasks))
    # wait for tasks to complete, basically just synchronizing call.
    t = [task.get() for task in tasks if task.ready() == True]
    # when t is full, the process has completed, so can chain onto next
    # function(fuzzer)
