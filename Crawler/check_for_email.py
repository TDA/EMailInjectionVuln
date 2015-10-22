from __future__ import absolute_import
from bs4 import BeautifulSoup
import re
import os
import urllib.request
import urllib.error
import urllib.parse
import urllib.parse
import socket
import ssl
import sys
import mysql.connector
from xml.dom import minidom
from Crawler.functions import *
from CeleryCrawler import Celery
from Crawler.celery import app

# This takes the feed from the queue and inserts into db if an email field is found
# I am particularly searching for the word 'email' instead of an email field.
# This is cause, at times, designers may have a text field with a label called email.
# Instead of an id/name/type of email. Accessibility isn't exactly their goal. ikr.
# :P :D
# Call this script from the terminal, while the worker is running, like so:
# check_for_email_field.delay([form_id,form_content]])
#


@app.task
def check_for_email_field(tuple):
    form_id = tuple[0]
    form_content = tuple[1]
    value = "email|e-mail"
    search_string = re.compile(value, re.IGNORECASE)
    if(re.search(search_string, form_content) != None):
        print("found somebody")
        # we found an email field, possibly
        # so, try inserting into the db
        # insertion might fail for duplicate form_ids
        # this is by design.
        try:

            db = getopenconnection()
            cursor = db.cursor()
            insert_query = insert_query_gen('email_forms', ('', form_id))
            cursor.execute(insert_query)
            db.commit()
        except Exception as e:
            print("Definitely a database issue, well, hopefully.")
            print(e)
            # just ignore and move on
            return
        return "Found"
