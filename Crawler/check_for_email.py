from __future__ import absolute_import
from bs4 import BeautifulSoup
import re
import os
import urllib.request, urllib.error, urllib.parse
import urllib.parse
import socket
import ssl
import sys
import mysql.connector
from xml.dom import minidom
from Crawler.functions import *
from celery import Celery
from Crawler.celery import app

# this is the code from the other file, fine tune it to read and write from the db
#email_fields=form.findAll(type="email")
        #if(len(email_fields)!=0):
            #do processing with the email fields
            #for f in email_fields:
                #print("Found a normal email field")
                #process_input(f,params)
#check if the input field is email field
                #if(check_input(inp,"email|e-mail")==True):
                #    print("Name or id was set to email")
                