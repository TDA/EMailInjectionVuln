from __future__ import absolute_import
__author__ = 'saipc'

import re
from Crawler.functions import *
from Fuzzer import fuzzer
import mock
import requests
import unittest

# THIS IS THE TEST DATA, NOT SURE IF THIS SHOULD BE INSIDE THE CLASS
# Sample data set
main_url = 'http://localhost:63343/htdocs/TestProject/email.htm'
attributes = [{'data-hi': 'hi'}]
# purposely left in CamelCase, we can later write tests
# for both uppercase and lowercase
method_1 = 'Get'
method_2 = 'Post'
# test both types of url in the form
action_1 = 'MailTest.php'
action_2 = 'http://localhost:63343/htdocs/TestProject/MailTest.php'

# test all types of input fields in the form
input_list_1 = [{'name': 'pass', 'value': '', 'element_type': 'input', 'type': 'password'},
                {'name': 'uname', 'value': '', 'element_type': 'input', 'type': 'text'},
                {'name': 'email', 'value': '', 'element_type': 'input', 'type': 'text'},
                {'name': '', 'value': 'Signup', 'element_type': 'input', 'type': 'submit'}]

input_list_2 = [{'name': 'pass', 'value': '', 'element_type': 'input', 'type': 'date'},
                {'name': 'uname', 'value': '', 'element_type': 'input', 'type': 'text'},
                {'name': 'mail', 'value': '', 'element_type': 'input', 'type': 'email'},
                {'name': '', 'value': 'Signup', 'element_type': 'input', 'type': 'submit'}]

input_list_3 = [{'name': 'pass', 'value': '', 'element_type': 'input', 'type': 'text'},
                {'name': 'uname', 'value': '', 'element_type': 'input', 'type': 'text'},
                {'name': 'mail', 'value': '', 'id': 'e-mail', 'element_type': 'input', 'type': 'text'},
                {'name': '', 'value': 'Signup', 'element_type': 'input', 'type': 'submit'}]

# this is the format : main_url, attributes, method, action, input_list = reconstructed_form

# fuzzer() is the thing we are testing here
# subclass the unittest.TestCase

class FuzzerTester(unittest.TestCase):
    # A testcase is created by subclassing unittest.TestCase. The individual
    # tests are defined with methods whose names start with the word "test".
    # This naming convention informs the test runner about which methods represent tests.

    # mock up the requests lib, no
    # need to generate actual requests
    requests = mock.Mock()
    requests.post = mock.Mock()

    def test_send_get_request(self):
        requests.get = mock.Mock()
        reconstructed_form = (main_url, attributes, method_1, action_1, input_list_1)
        fuzzer.fuzzer(reconstructed_form)
        assert(requests.get.called)

        # upper case GET
        reconstructed_form = (main_url, attributes, method_1.upper(), action_1, input_list_1)
        fuzzer.fuzzer(reconstructed_form)
        assert(requests.get.called)

        # lower case GET
        reconstructed_form = (main_url, attributes, method_1.lower(), action_1, input_list_1)
        fuzzer.fuzzer(reconstructed_form)
        assert(requests.get.called)


# to run a main program inside the modules, run like so:
# python3 -m Tests.email_form_retriever_tests
# with verbosity, python3 -m Tests.email_form_retriever_tests --verbose OR -v
if __name__ == '__main__':
    # print("hello")
    unittest.main()

def start_test():
    print("Test Started")
    unittest.main()


reconstructed_form = ()