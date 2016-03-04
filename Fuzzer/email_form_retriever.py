from __future__ import absolute_import

__author__ = 'saipc'

import ast
from celery import Celery

from functions import *
from CeleryFuzzer import app
from fuzzer import *

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
        # print(duplicate_search_query)
        cursor.execute(duplicate_search_query)

        duplicate_rows = cursor.fetchall()
        if len(duplicate_rows) > 0:
            # print(duplicate_rows)
            # means this form_id is already in the fuzzed_forms table => fuzzed
            # print("Form with form_id %s ALREADY FUZZED!!! returning without further checks" % str(form_id))
            # close the db connection
            db.close()
            return "Form with form_id %s ALREADY FUZZED!!!" % str(form_id)

        # retrieve that form
        FORM_TABLE_NAME = 'form'
        # we need the main url too
        search_query = generate_search_query(FORM_TABLE_NAME, 'url, attributes, method, absolute_action, params', 'id', str(form_id))
        cursor.execute(search_query)

        # TODO: this SHOULD return only one row, might need to change this
        # WOULDNT REALLY AFFECT PERFORMANCE, AS IT HAS ONLY ONE ROW ANYWAY
        rows = cursor.fetchall()

        tasks = []
        # http://www.w3.org/TR/html401/interact/forms.html#h-17.13.3
        # these are the steps to reconstruct a form (as done by browser)
        # here we need to retrieve the actual form fields and reconstruct the form
        for row in rows:
            reconstructed_form = reconstruct_form(cursor, row)
            tasks.append(call_fuzzer_with_payload.delay(reconstructed_form, form_id))
            # fuzzer(reconstructed_form)
            # have to write up the fuzzer --> DONE
        db.commit()
        db.close()
        return "Success"

    except Exception as e:
        print("Definitely a database issue, well, hopefully. We are in %s" % (__name__))
        print(e)
        with open('log_fuzzer', 'a') as file_handle:
            file_handle.write(str(e) + '\n' + "We are in %s" % (__name__) + '\n')
    return


