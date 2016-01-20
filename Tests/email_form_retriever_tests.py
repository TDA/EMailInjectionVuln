from __future__ import absolute_import
__author__ = 'saipc'

from bs4 import BeautifulSoup
import re
import ast
import mysql.connector

from Crawler.functions import *
from Fuzzer.call_email_form_retriever import call_email_form_retriever


import unittest

# call_email_form_retriever() is the thing we are testing here
# subclass the unittest.TestCase
class KnownEMailValues(unittest.TestCase):
    actual_output = ''
    expected_output = ''

# to run a main program inside the modules, run like so:
# python3 -m Tests.email_form_retriever_tests
if __name__ == '__main__':
    print("hello")
    unittest.main()

def start_test():
    print("Test Started")
    unittest.main()