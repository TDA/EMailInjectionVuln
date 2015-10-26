from __future__ import absolute_import
__author__ = 'saipc'
from bs4 import BeautifulSoup
import re
import ast
import mysql.connector
from celery import Celery

from Crawler.functions import *
from Fuzzer.fuzzer import fuzzer
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
        cursor.execute(search_query)
        rows = cursor.fetchall()
        tasks = []
        # http://www.w3.org/TR/html401/interact/forms.html#h-17.13.3
        # these are the steps to reconstruct a form (as done by browser)
        for row in rows:
            # this complicated looking line basically converts the
            # string into a list, and gets the first element of the
            # list, which is actually a dictionary, i have no idea
            # why i saved it that way in the db, but i think cuz json --> Fixed this in functions
            attributes = ast.literal_eval(row[0])

            method = row[1]
            action = row[2]
            params = row[3]
            # lets you reconstruct a list from its string representation
            params = ast.literal_eval(params)
            for param in params:
                print(param)

            # here we need to retrieve the actual form fields and reconstruct the form
            #tasks.append(fuzzer.delay(row))

        db.commit()

    except Exception as e:
        print("Definitely a database issue, well, hopefully.")
        print(e)
        return


