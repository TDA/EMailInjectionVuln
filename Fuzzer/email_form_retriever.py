from __future__ import absolute_import
__author__ = 'saipc'
from bs4 import BeautifulSoup
import re
import mysql.connector
from celery import Celery

from Crawler.functions import *
from Fuzzer.CeleryFuzzer import app

@app.task(name='Fuzzer.email_form_retriever')
def email_form_retriever():
    try:
        db = getopenconnection()
        cursor = db.cursor()
        # Lets get all the email forms from the db and print them for now
        TABLE_NAME = 'email_forms'
        search_query = generate_search_query(TABLE_NAME, 'id, form_id', 'form_id', 1)
        print(search_query)
        # cursor.execute(search_query)
        db.commit()

    except Exception as e:
        print("Definitely a database issue, well, hopefully.")
        print(e)
        return


