from __future__ import absolute_import
__author__ = 'saipc'

import re

from Crawler.functions import *

import unittest
import mock

def hello():
    print("hello")

# call_email_form_retriever() is the thing we are testing here
# subclass the unittest.TestCase
class KnownEMailValues(unittest.TestCase):
    # A testcase is created by subclassing unittest.TestCase. The individual
    # tests are defined with methods whose names start with the word "test".
    # This naming convention informs the test runner about which methods represent tests.
    @mock.patch('email_form_retriever_tests.hello')
    def test_is_equal_values(self, mock_hello):
        actual_output = ''
        expected_output = ''
        # self.assertEqual(actual_output, expected_output)
        self.assertEqual("foo", "foo", "foo is not equal to foo")
        hello()
        mock_hello.assert_has_calls()

# to run a main program inside the modules, run like so:
# python3 -m Tests.email_form_retriever_tests
# with verbosity, python3 -m Tests.email_form_retriever_tests --verbose OR -v
if __name__ == '__main__':
    # print("hello")
    unittest.main()

def start_test():
    print("Test Started")
    unittest.main()