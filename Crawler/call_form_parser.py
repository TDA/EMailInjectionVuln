from __future__ import absolute_import
from bs4 import BeautifulSoup
import re
import os
import socket
import ssl
import sys
import mysql.connector
from celery import Celery

from Crawler.functions import *
from Crawler.check_for_email import check_for_email_field
from Crawler.form_parser import form_parse
from Crawler.call_check_for_email import call_check_for_email

from Crawler.CeleryCrawler import app

# convenience function to call the form_parser and once its done with its
# form_parsing, call the call_check_for_email function which will in turn call the
# check_email_fields in a celery-concurrent way.


@app.task
def call_fp(urls):
    tasks = []
    for url in urls:
        # just call the form_parse method in celery style so that it runs
        # concurrently
        tasks.append(form_parse.delay(url))
    print(len(tasks))
    # wait for tasks to complete, basically just synchronizing call.
    t = [task.get() for task in tasks if task.ready() == True]
    print(t)
    # when t is full, the process has completed, so can chain onto next
    # function(call_check_for_email), which will in turn check for the email forms
    call_check_for_email()
