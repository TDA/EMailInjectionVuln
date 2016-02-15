from __future__ import absolute_import
__author__ = 'saipc'
from celery import Celery

from functions import *
from email_form_retriever import email_form_retriever
from CeleryFuzzer import app

# from Fuzzer.call_email_form_retriever import call_email_form_retriever
# call_email_form_retriever.delay()

@app.task(name='Fuzzer.call_email_form_retriever')
def call_email_form_retriever():
    try:
        db = getopenconnection()
        cursor = db.cursor()
        # Lets get all the email forms from the db and print them for now
        TABLE_NAME = 'email_forms'
        search_query = generate_search_query(TABLE_NAME)
        print(search_query)
        cursor.execute(search_query)
        rows = cursor.fetchall()
        print(rows[0])
        tasks = []
        for row in rows:
            # here we need to retrieve the actual form fields
            # and reconstruct the forms to be fuzzed
            tasks.append(email_form_retriever.delay(row))
            # email_form_retriever(row)
        db.commit()

    except Exception as e:
        print("Definitely a database issue, well, hopefully. We are in %s" % (__name__))
        print(e)
        with open('log_fuzzer', 'a') as file_handle:
            file_handle.write(str(e))
        return


