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

def start_test():
    print("Test Started")
    unittest.main()
