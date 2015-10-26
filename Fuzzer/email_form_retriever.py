from __future__ import absolute_import
__author__ = 'saipc'
from bs4 import BeautifulSoup
import re
import mysql.connector
from celery import Celery

from Crawler.functions import *
from Fuzzer.CeleryFuzzer import app

@app.task(name='Fuzzer.email_form_retriever')
def email_form_retriever(row):
    try:
        form_id = row[1]
        db = getopenconnection()
        cursor = db.cursor()
        # Lets get all the email forms from the db and print them for now
        TABLE_NAME = 'form'
        search_query = generate_search_query(TABLE_NAME, 'attributes, method, absolute_action, params', 'id', str(form_id))
        print(search_query)
        #cursor.execute(search_query)
        #rows = cursor.fetchall()
        #tasks = []
        #for row in rows:
            # here we need to retrieve the actual form fields and reconstruct the
         #   tasks.append(email_form_retriever.delay(row))


        db.commit()

    except Exception as e:
        print("Definitely a database issue, well, hopefully.")
        print(e)
        return


