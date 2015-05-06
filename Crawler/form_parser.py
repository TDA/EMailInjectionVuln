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


#app = Celery('form_parser', broker='amqp://guest@localhost//')

@app.task
def form_parse(url):

    page = None
    headers = None
    
    try:
        page = urllib.request.urlopen(url).read()
    except Exception:
        print ("Could not open/read the page")
        return
    try:
        soup = BeautifulSoup(page)
    except Exception as e:
        print ("Error: error with BeautifulSoup")
        return

    method = None
    attributes = []
    absolute_action= None
    action = None
    params = set()
    request_id = None
    form_id=None
    xpath = None
    req_id = None
    input_names = []
    base_url = None
    base_tag = soup.select('html > head > base')
    if base_tag:
        the_base_tag = base_tag[0]
        if the_base_tag.has_attr("href"):
            base_url = the_base_tag["href"]

    forms = soup.findAll('form')
    for form in forms:
        # write code to iterate through each form on the page and store them
        #print(form)
        
        inputs = form.findAll('input')
        if(len(inputs)>0):
            for inp in inputs:
                #print(inp.attrs)
                #do input processing and store the inputs in the db, saving a reference to the form_id
                process_input(inp,params)


        #for p in params:
        #    print(p)
        if(len(params)>0):
            #means we have atleast one email field. yay!
            #extract info from the form
            #store in db
            method,action,attributes=extract_form_attrs(form)
            #find the absolute action if the base url was set
            if base_url!=None:
                absolute_action=base_url+action
            else:
                absolute_action=action
            #find and set the request id so that we can enter it into the db
            
        #do we store only the input ids in the inputs table or do we store the actual input or only names?
        #I would say only input ids, and for all inputs in the form, or else we wont be able to reconstruct the form later.
        print('',url,attributes,req_id,form,method,action,absolute_action)
        #print("is this there?")
        try:
            db = mysql.connector.connect(user='root', password='',
                                  host='localhost',
                                  database='ejection')
            cursor = db.cursor()
            #store_url() needs to be called here, stores the url in the requests table
            #write a generic function to generate queries maybe?
            insert_query="insert into requests values('','"+str(headers)+"','"+str(url)+"')"
            cursor.execute(insert_query)
            req_id=cursor.lastrowid
            db.commit()

            store_form(('',url,attributes,req_id,form,method,action,absolute_action))
            #cursor.execute(query)
        #for a in cursor:
            #print(a)
        except Exception as e:
            print ("Could not connect to database")
            print (e)
            return
        #print("and this?")
        print(req_id)

        #store_form() needs to be called here, pass the whole thing as a dict? or list?
        #configuring the database with queues might need some code, check that out sai.
        #store_params() needs to be called in a loop here to store all the params, (or executeALL if supported)


#form_parse(r'http://localhost/VV/vv.htm')