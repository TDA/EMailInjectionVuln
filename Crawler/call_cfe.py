from __future__ import absolute_import
from bs4 import BeautifulSoup
import re
import os
import urllib.request
import urllib.error
import urllib.parse
import socket
import ssl
import sys
import mysql.connector
from xml.dom import minidom
from Crawler.functions import *
from Crawler.check_for_email import check_for_email_field
from Crawler.form_parser import form_parse
from celery import Celery
from Crawler.celery import app

# open a db connection and retrieve all the forms that need to be checked
# if they actually contain email fields, this starts up a celery
# concurrent program
@app.task
def call_cfe():
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
