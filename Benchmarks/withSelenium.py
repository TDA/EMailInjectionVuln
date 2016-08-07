import re

__author__ = 'saipc'


from selenium import webdriver

# Launching web driver instance
driver = webdriver.Firefox()
random_url = 'https://en.wikipedia.org/wiki/Special:Random'

# for loop to load random wikipedia articles
for page_number in xrange(1000):
    # Loading en.wikipedia random page article
    driver.get(random_url)

    src = driver.page_source
    # check if theres an input field
    # is_email_present = re.search(r'email|e-mail|mail', src)

    # The URL for this article
    page_url = driver.current_url

    task = '%4d: ' % (page_number+1)
    print '------------------------------------'
    # print task + 'Input field?: ' + str(is_email_present)
    print task + 'Page url: ' + page_url
    print '------------------------------------'
    print

# Close web driver instance
driver.close()