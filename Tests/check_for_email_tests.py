from __future__ import absolute_import
__author__ = 'saipc'

from Crawler.functions import *
from Crawler import check_for_email
import mock
import unittest

class CheckForEmailTester(unittest.TestCase):
    @mock.patch("mysql.connector.connect")
    def test_db_connection_called(self, cursor):
        retValue = check_for_email.check_for_email_field([1, "<form><input type=email></form"])
        self.assertTrue(cursor.called, "Cursor never called")

    @mock.patch("mysql.connector.connect")
    def test_check_for_email(self, cursor):
        retValue = check_for_email.check_for_email_field([1, "<form><input type=email></form"])
        self.assertEqual(retValue, "Found")
        retValue = check_for_email.check_for_email_field([1, "<form><input type=e-mail></form"])
        self.assertEqual(retValue, "Found")


# python3 -m Tests.form_parser_tests
# with verbosity, python3 -m Tests.form_parser_tests --verbose OR -v
if __name__ == '__main__':
    # print("hello")
    unittest.main()
