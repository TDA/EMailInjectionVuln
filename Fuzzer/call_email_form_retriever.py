from __future__ import absolute_import
__author__ = 'saipc'
import mysql.connector
from celery import Celery

from Crawler.functions import *
from Fuzzer.email_form_retriever import email_form_retriever
from Fuzzer.CeleryFuzzer import app

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
        tasks = []
        for row in rows:
            # here we need to retrieve the actual form fields
            # and reconstruct the forms to be fuzzed
            tasks.append(email_form_retriever.delay(row))
        db.commit()

    except Exception as e:
        print("Definitely a database issue, well, hopefully.")
        print(e)
        return


