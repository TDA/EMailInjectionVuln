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

def reconstruct_form(cursor, row):
    # this complicated looking line basically converts the --> nvm
    # string into a list, and gets the first element of the --> nvm
    # list, which is actually a dictionary, i have no idea --> nvm
    # why i saved it that way in the db, but i think cuz json --> Fixed this in functions
    main_url = row[0]
    # now attributes is just a dict
    attributes = ast.literal_eval(row[1])
    method = row[2]
    action = row[3]
    params = row[4]
    # lets you reconstruct a list from its string representation
    params = ast.literal_eval(params)
    input_list = []
    for param_id in params:
        TABLE_NAME = 'params'
        param_search_query = generate_search_query(TABLE_NAME, 'element_type, type, name, value', 'id', str(param_id))
        print(param_search_query)
        cursor.execute(param_search_query)
        param_row = cursor.fetchone()
        if param_row == None or (len(param_row)) == 0:
            # no such params stored, return
            continue
        # construct a dict of the params of each input and append to list
        param_dict = {'element_type' : param_row[0],
                      'type' : param_row[1],
                      'name' : param_row[2],
                      'value': param_row[3]}
        input_list.append(param_dict)
    # now we have all the data to reconstruct the form and fuzz it
    # send this as an immutable tuple
    reconstructed_form = (main_url, attributes, method, action, input_list)

@app.task(name='Fuzzer.email_form_retriever')
def email_form_retriever(row):
    try:
        form_id = row[1]
        db = getopenconnection()
        cursor = db.cursor()

        # this should also check whether the form is already in the
        # fuzzed_forms table, if so, skip and continue
        FUZZED_FORMS_TABLE_NAME = 'fuzzed_forms'
        duplicate_search_query = generate_search_query(FUZZED_FORMS_TABLE_NAME, '', 'form_id', str(form_id))
        print(duplicate_search_query)
        cursor.execute(duplicate_search_query)

        duplicate_rows = cursor.fetchall()
        if len(duplicate_rows) > 0:
            print(duplicate_rows)
            # means this form_id is already in the fuzzed_forms table => fuzzed
            print("Form with form_id %s ALREADY FUZZED!!! returning without further checks" % str(form_id))
            return

        # Lets get all the email forms from the db and print them for now
        FORM_TABLE_NAME = 'form'
        # we need the main url too
        search_query = generate_search_query(FORM_TABLE_NAME, 'url, attributes, method, absolute_action, params', 'id', str(form_id))
        print(search_query)
        cursor.execute(search_query)

        # TODO: this SHOULD return only one row, might need to change this
        rows = cursor.fetchall()

        tasks = []
        # http://www.w3.org/TR/html401/interact/forms.html#h-17.13.3
        # these are the steps to reconstruct a form (as done by browser)
        # here we need to retrieve the actual form fields and reconstruct the form
        for row in rows:
            reconstructed_form = reconstruct_form(cursor, row)
            #tasks.append(fuzzer.delay(reconstructed_form))
            fuzzer(reconstructed_form)
            # have to write up the fuzzer --> DONE

        db.commit()

    except Exception as e:
        print("Definitely a database issue, well, hopefully. We are in %s" % (__name__))
        print(e)
    return


