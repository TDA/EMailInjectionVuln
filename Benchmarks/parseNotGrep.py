import requests

__author__ = 'saipc'

import time
from bs4 import BeautifulSoup
import re

random_url = 'https://en.wikipedia.org/wiki/Special:Random'

def check_input(input, value):
    search_string = re.compile(value, re.IGNORECASE)
    is_present = False
    if(input.get('name') != None):
        is_present = (re.search(search_string, input.get('name')) != None)
    if(input.get('id') != None):
        # if already found, we should not reset it to false later
        is_present = is_present or (re.search(search_string, input.get('id')) != None)
    if(input.get('type') != None):
        is_present = is_present or (re.search(search_string, input.get('type')) != None)
    return is_present
    # returns true if the input field has name OR id
    # OR type set to be the 'value' provided,
    # else returns false.

start_time = time.time()
# for loop to load random wikipedia articles
for page_number in xrange(1000):
    is_email_present = None
    # Loading en.wikipedia random page article
    r = requests.get(random_url)

    src = BeautifulSoup(r.text, 'html.parser')
    # check if theres an input field
    forms = src.find_all('form')
    for form in forms:
        input_fields = form.find_all('input')
        for input in input_fields:
            is_email_present = check_input(input, 'email|e-mail|mail')
            if is_email_present:
                break

    

    # The URL for this article
    page_url = random_url

    task = '%4d: ' % (page_number+1)
    print '------------------------------------'
    print task + 'Input field?: ' + str(is_email_present)
    print task + 'Page url: ' + page_url
    print '------------------------------------'

end_time = time.time()
elapsed_time = end_time - start_time
print "Start time: " + str(start_time)
print "End time: " + str(end_time)
print "Total elapsed time: " + str(elapsed_time)