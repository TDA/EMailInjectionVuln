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
    # A testcase is created by subclassing unittest.TestCase. The individual
    # tests are defined with methods whose names start with the letters test.
    # This naming convention informs the test runner about which methods represent tests.
    def test_is_equal_values(self):
        actual_output = ''
        expected_output = ''
        # self.assertEqual(actual_output, expected_output)
        self.assertEqual("foo", "foo", "foo is not equal to foo")

# to run a main program inside the modules, run like so:
# python3 -m Tests.email_form_retriever_tests
# with verbosity, python3 -m Tests.email_form_retriever_tests --verbose OR -v
if __name__ == '__main__':
    # print("hello")
    unittest.main()

def start_test():
    print("Test Started")
    unittest.main()