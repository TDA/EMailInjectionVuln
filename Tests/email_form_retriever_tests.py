from __future__ import absolute_import
__author__ = 'saipc'

from Crawler.functions import *
import unittest
import mock
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

    def test_reconstruct_form(self):
        cursor = mock.MagicMock(name='cursor')
        row = (main_url, attributes, method, action, "[]")
        expected_reconstructed_form = (main_url, attributes_dict, method, action, [])
        reconstructed_form = email_form_retriever.reconstruct_form(cursor, row)
        # print(reconstructed_form)
        self.assertEqual(expected_reconstructed_form, reconstructed_form, "Form was not formed properly")

    @mock.patch('Fuzzer.email_form_retriever.fuzzer')
    def test_email_form_retriever_already_fuzzed(self, fuzzer):
        # NOTE: this REQUIRES THE DATABASE TO BE RUNNING
        # form_id 5 has been fuzzed already
        row = [1, 5]
        data = email_form_retriever.email_form_retriever(row)
        self.assertEqual(data, "Form with form_id 5 ALREADY FUZZED!!!", "Fuzzed form not detected")
        self.assertFalse(fuzzer.called, "Error: Fuzzer was called")

    # this patch due to namespace conflict :)
    @mock.patch('Fuzzer.email_form_retriever.fuzzer')
    def test_email_form_retriever_calls_fuzzer_for_new_fuzz(self, fuzzer):
        # NOTE: this REQUIRES THE DATABASE TO BE RUNNING
        # form_id 42 has NOT been fuzzed
        url = "http://localhost/VV/vv.htm"
        attributes = [{"name": "f2", "onsubmit": "do()"}]
        method = "GET"
        action = "iamsaipc/"
        input_list = [{'element_type': 'input', 'value': '', 'type': 'text', 'name': 'uname2'},
                    {'element_type': 'input', 'value': '', 'type': 'email', 'name': 'uname'}]
        row = [1, 42]
        data = email_form_retriever.email_form_retriever(row)
        # test the fuzzer gets called, changed this to fuzzer.delay, cuz Celery
        self.assertTrue(fuzzer.delay.called, "Fuzzer did not get called")
        # test that the fuzzer was called
        # with the right params
        fuzzer.delay.assert_called_with((url,attributes, method, action, input_list))
        # test that the return data was correct
        self.assertEqual(data, "Success")


# to run a main program inside the modules, run like so:
# python3 -m Tests.email_form_retriever_tests
# with verbosity, python3 -m Tests.email_form_retriever_tests --verbose OR -v
if __name__ == '__main__':
    # print("hello")
    unittest.main()

def start_test():
    print("Test Started")
    unittest.main()