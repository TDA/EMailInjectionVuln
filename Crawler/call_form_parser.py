from __future__ import absolute_import
from celery import Celery

from functions import *
from form_parser import form_parse
from call_check_for_email import call_check_for_email

from CeleryCrawler import app

# convenience function to call the form_parser and once its done with its
# form_parsing, call the call_check_for_email function which will in turn call the
# check_email_fields in a celery-concurrent way.

# IMPORTANT: THIS IS THE FIRST THING TO BE CALLED FOR THE CRAWLER-PARSER, call this like so:
# from Crawler.call_form_parser import call_fp
# call_fp.delay([<urls>])
import crawler_listener

@app.task(name='Crawler.call_form_parser')
class Starter:

    how_many = 0

    def __init__(self):
        pass

    def callback(self, crawled_url):
        print(" [%d urls] Received %d bytes from %r" % (self.how_many,
                len(crawled_url.content),crawled_url.url))
        print ("URL", crawled_url.url)
        tasks = []
        tasks.append(form_parse.delay(crawled_url.url, crawled_url.content))
        self.how_many += 1
        t = [task.get() for task in tasks if task.ready() == True]
        print(t)
        # when t is full, the process has completed, so can chain onto next
        # function(call_check_for_email), which will in turn check for the email forms
        call_check_for_email()

if __name__ == '__main__':
    crawler_listener.add_callback(Starter().callback)

# def call_fp(urls):
#
#     for url in urls:
#         # just call the form_parse method in celery style so that it runs
#         # concurrently
#         tasks.append(form_parse.delay(url, html_content))
#     print(len(tasks))
#     # wait for tasks to complete, basically just synchronizing call.
#     t = [task.get() for task in tasks if task.ready() == True]
#     print(t)
#     # when t is full, the process has completed, so can chain onto next
#     # function(call_check_for_email), which will in turn check for the email forms
#     call_check_for_email()
