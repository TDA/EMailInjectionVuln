from __future__ import absolute_import
__author__ = 'saipc'

from bs4 import BeautifulSoup
import re
import ast
import mysql.connector
from celery import Celery

from Crawler.functions import *
from Fuzzer.fuzzer import fuzzer
from Fuzzer.CeleryFuzzer import app

import unittest
