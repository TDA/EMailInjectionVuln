from __future__ import absolute_import
__author__ = 'saipc'

import re

from Crawler.functions import *

import unittest
import mock
from Tests import fuzzer_tests
from Fuzzer import email_form_retriever

main_url = 'http://localhost:63343/htdocs/TestProject/email.htm'
# set this as a string cuz the script will parse
# this as an ast into a dict
attributes = "[{'data-hi': 'hi'}]"
attributes_dict = [{'data-hi': 'hi'}]
method = 'Get'
action = 'http://localhost:63343/htdocs/TestProject/MailTest.php'
test_payload = 'saiprash_thegreatest@yahoo.co.in%0Abcc:schand31@asu.edu'

# test all types of input fields in the form
input_list_1 = [{'name': 'pass', 'value': '', 'element_type': 'input', 'type': 'password'},
                {'name': 'uname', 'value': '', 'element_type': 'input', 'type': 'text'},
                {'name': 'email', 'value': '', 'element_type': 'input', 'type': 'text'},
                {'name': '', 'value': 'Signup', 'element_type': 'input', 'type': 'submit'}]

# call_email_form_retriever() is the thing we are testing here
# subclass the unittest.TestCase
class EMailFormRetrieverTester(unittest.TestCase):
    # A testcase is created by subclassing unittest.TestCase. The individual
    # tests are defined with methods whose names start with the word "test".
    # This naming convention informs the test runner about which methods represent tests.
    fuzzer_tests.hello = mock.Mock()
    def test_is_equal_values(self):
        # self.assertEqual(actual_output, expected_output)
        self.assertEqual("foo", "foo", "foo is not equal to foo")
        fuzzer_tests.hello()
        assert(fuzzer_tests.hello.called)

    def test_reconstruct_form(self):
        cursor = mock.Mock()
        row = (main_url, attributes, method, action, "[]")
        expected_reconstructed_form = (main_url, attributes_dict, method, action, [])
        reconstructed_form = email_form_retriever.reconstruct_form(cursor, row)
        # print(reconstructed_form)
        self.assertEqual(expected_reconstructed_form, reconstructed_form, "Form was not formed properly")

    def test_email_form_retriever(self):
        # NOTE: this REQUIRES THE DATABASE TO BE RUNNING
        fuzzer = mock.Mock()
        row = [01, 5]


# to run a main program inside the modules, run like so:
# python3 -m Tests.email_form_retriever_tests
# with verbosity, python3 -m Tests.email_form_retriever_tests --verbose OR -v
if __name__ == '__main__':
    # print("hello")
    unittest.main()

def start_test():
    print("Test Started")
    unittest.main()