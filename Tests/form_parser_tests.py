from __future__ import absolute_import
__author__ = 'saipc'

from Crawler.functions import *
from Crawler import form_parser
import mock
import unittest

class FormParserTester(unittest.TestCase):
    requests = mock.Mock()
    def test_url_exception(self):
        url = "bad url dadadadada"
        # form_parser.form_parse(url)
        exc = form_parser.form_parse(url)
        self.assertEqual(exc, "Could not open/read the page")

    @mock.patch("mysql.connector.connect")
    def test_db_connection(self, mysql):
        url = "http://google.com"
        # form_parser.form_parse(url)
        exc = form_parser.form_parse(url)
        # test that the connection is created
        self.assertTrue(mysql.called, "DB connection not called")
        # test that the connection is created
        # with the right attributes
        mysql.assert_called_with(user='root', password='',
                                   host='localhost',
                                   database='ejection')

        # with the right attributes
# to run a main program inside the modules, run like so:
# python3 -m Tests.form_parser_tests
# with verbosity, python3 -m Tests.form_parser_tests --verbose OR -v
if __name__ == '__main__':
    # print("hello")
    unittest.main()
