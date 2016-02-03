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
test_payload = 'saiprash_thegreatest@yahoo.co.in%0Abcc:schand31@asu.edu'

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
                {'name': 'madam', 'value': '', 'id': 'e-mail', 'element_type': 'input', 'type': 'text'},
                {'name': '', 'value': 'Signup', 'element_type': 'input', 'type': 'submit'}]


input_list_4 = [{'name': 'pass', 'value': '', 'element_type': 'input', 'type': 'text'},
                {'name': 'uname', 'value': '', 'element_type': 'input', 'type': 'text'},
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

    def test_construct_url(self):
        # check if both produce the same final url
        url1 = fuzzer.construct_url(action_1, main_url)
        url2 = fuzzer.construct_url(action_2, main_url)
        self.assertEqual(url1, url2, "The generated URLS are not the same")

    def test_send_get_request(self):
        requests.get = mock.Mock()
        reconstructed_form = (main_url, attributes, method_1, action_1, input_list_1)
        fuzzer.fuzzer(reconstructed_form)
        self.assertTrue(requests.get.called, "Get request failed")

        # upper case GET
        reconstructed_form = (main_url, attributes, method_1.upper(), action_1, input_list_1)
        fuzzer.fuzzer(reconstructed_form)
        self.assertTrue(requests.get.called, "GET request failed")

        # lower case GET
        reconstructed_form = (main_url, attributes, method_1.lower(), action_1, input_list_1)
        fuzzer.fuzzer(reconstructed_form)
        self.assertTrue(requests.get.called, "get request failed")

    def test_send_post_request(self):
        requests.post = mock.Mock()
        reconstructed_form = (main_url, attributes, method_2, action_1, input_list_1)
        fuzzer.fuzzer(reconstructed_form)
        self.assertTrue(requests.post.called, "Post request failed")

        # upper case POST
        reconstructed_form = (main_url, attributes, method_2.upper(), action_1, input_list_1)
        fuzzer.fuzzer(reconstructed_form)
        self.assertTrue(requests.post.called, "POST request failed")

        # lower case POST
        reconstructed_form = (main_url, attributes, method_2.lower(), action_1, input_list_1)
        fuzzer.fuzzer(reconstructed_form)
        self.assertTrue(requests.post.called, "post request failed")

    def test_correct_fuzzer_data(self):
        requests.get = mock.Mock()
        requests.post = mock.Mock()
        # check if the fuzzer is injecting the data properly
        # even if the fields are different etc
        # input_list_1 needs to have payload in the "email" field
        reconstructed_form = (main_url, attributes, method_1, action_1, input_list_1)
        data = fuzzer.fuzzer(reconstructed_form)
        # print("HERES THE RECEIVED DATA", data)
        # now data needs to contain the test payload
        self.assertEqual(test_payload, data["email"], "Payload is incorrect")

        # input_list_2 needs to have payload in the mail field
        reconstructed_form = (main_url, attributes, method_1, action_1, input_list_2)
        data = fuzzer.fuzzer(reconstructed_form)
        # now data needs to contain the test payload
        self.assertEqual(test_payload, data["mail"], "Payload is incorrect")

        # input_list_3 needs to have payload in the madam field
        reconstructed_form = (main_url, attributes, method_1, action_1, input_list_3)
        data = fuzzer.fuzzer(reconstructed_form)
        # now data needs to contain the test payload
        self.assertEqual(test_payload, data["madam"], "Payload is incorrect")

    def test_incorrect_fuzzer_data(self):
        requests.get = mock.Mock()
        requests.post = mock.Mock()
        reconstructed_form = (main_url, attributes, method_1, action_1, input_list_4)
        data = fuzzer.fuzzer(reconstructed_form)
        # test if the fuzzer injects stuff when no email is present
        values = [data[key] for key in data]
        # print(values)

        self.assertTrue(test_payload not in values, "Payload injected incorrectly")


# to run a main program inside the modules, run like so:
# python3 -m Tests.fuzzer_tests
# with verbosity, python3 -m Tests.fuzzer_tests --verbose OR -v
if __name__ == '__main__':
    # print("hello")
    unittest.main()

def start_test():
    print("Test Started")
    unittest.main()
