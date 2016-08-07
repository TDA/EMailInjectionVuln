import requests

__author__ = 'saipc'

import time
from bs4 import BeautifulSoup
import re

random_url = 'https://en.wikipedia.org/wiki/Special:Random'

start_time = time.time()
# for loop to load random wikipedia articles
for page_number in xrange(1000):
    # Loading en.wikipedia random page article
    r = requests.get(random_url)

    src = BeautifulSoup(r.text, 'html.parser')
    # check if theres an input field
    is_email_present = re.search(r'email|e-mail|mail', src.text)

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