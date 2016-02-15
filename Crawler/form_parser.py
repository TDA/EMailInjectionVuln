from __future__ import absolute_import
from bs4 import BeautifulSoup
from celery import Celery
from functions import *
from CeleryCrawler import app
from check_for_email import check_for_email_field


# app = Celery('form_parser', broker='amqp://guest@localhost//')
# Run the app like so, start the worker in the directory above:
# celery -A CeleryCrawler worker --loglevel=info
# call the task like so:
# form_parse.delay(url)
# all print statements are for logging purposes only, can be removed
@app.task(name='Crawler.form_parser')
def form_parse(url, html_content):
    # print(url)
    page = html_content
    # headers = None
    # try:
    #     # no idea why this uses urllib instead of requests
    #     req = urllib.request.Request(url)
    #     req.add_header('Referer', req.origin_req_host)
    #     req.add_header('User-Agent', 'Mozilla/5.0')
    #
    #     resp = urllib.request.urlopen(req)
    #     page = resp.read()
    #     # json dump to escape single quotes and store as list/dict.
    #     headers = json.dumps(req.header_items())
    #     # could be 400/500 and still wont result in any problem at all.
    #     # print (resp.status)
    #     # print (headers)
    # except Exception as e:
    #     # exit if the page couldnt be read.
    #     # print("Could not open/read the page")
    #     print(e)
    #     return("Could not open/read the page")
    try:
        soup = BeautifulSoup(page, "html.parser")
    except Exception as e:
        print("Error: error with BeautifulSoup")
        # once again, parsing errors mean page might not work, so better to
        # terminate
        return
    # set all the variables we are going to store to a default of None
    method = None
    absolute_action = None
    action = None
    request_id = None
    form_id = None
    xpath = None
    req_id = None
    base_url = None
    base_tag = soup.select('html > head > base')
    if base_tag:
        # check for base tag and store that if present, will affect all the
        # urls on the page so.
        the_base_tag = base_tag[0]
        if the_base_tag.has_attr("href"):
            base_url = the_base_tag["href"]

    forms = soup.findAll('form')
    # Code to iterate through each form on the page and store them
    for form in forms:
        # Set these variables here as there may be multiple forms on the page
        # and we want to store each ones separately.
        attributes = {}
        params = set()
        param_ids = list()
        inputs = form.findAll('input')
        # Check if any input exists within the form, else skip.
        if (len(inputs) > 0):
            for inp in inputs:
                # Processes each input and gives the name,type,value etc of
                # each input
                process_input(inp, params)

        # for p in params:
        # print(p)
        if (len(params) > 0):
            # means we have atleast one input field. yay!
            # extract info from the form
            # Give this a default of GET in case method isn't found on the
            # page.
            method = form.get('method') or 'GET'
            # what happens if no action is specified? do we use the same url? or the same path?
            # i.e: url or req.selector? I am leaving this empty for now.
            action = form.get('action') or ''
            # extract all the other attributes in the form tag, like javascript
            # handlers and such, not really required for our project, but might
            # be useful for some other research, maybe a prevalence of js
            # validation and its ineffectiveness :P :D

            attributes = extract_form_attrs(form)
            # find the absolute action if the base url was set
            if base_url != None:
                absolute_action = base_url + action
            else:
                absolute_action = action
                # find and set the request id so that we can enter it into the
                # db

        # do we store only the input ids in the inputs table or do we store the actual input or only names?
        # I would say only input ids, and for all inputs in the form, or else we wont be able to reconstruct the form later.
        # print('',url,attributes,req_id,form,method,action,absolute_action)
        # print("is this there?")
        try:
            db = getopenconnection()
            cursor = db.cursor()
            # Generic function to generate queries, is not foolproof, just
            # convenient. Forgive me, Master :D
            for param in params:
                param_insert_query = insert_query_gen('params', param)
                # print(param_insert_query)
                # insert every input field found into the db and store their
                # ids so that we can connect them to the forms table.
                cursor.execute(param_insert_query)
                last_param_id = cursor.lastrowid
                # lastrowid is a cool way to get the last inserted elements id
                param_ids.append(last_param_id)

            # store the requests' headers we used to fetch the page,
            # once again not really needed unless we use this for some other research.
            # the urls ARE required though.
            req_insert_query = insert_query_gen('requests', ('', url))
            cursor.execute(req_insert_query)
            req_id = cursor.lastrowid

            # actual storage of the forms and all the extracted details,
            # storing as much data as we can. Might be useful for future parts
            # of the project.
            # using json.dumps so that the single quotes in the dict key:value pairs don't
            # mess with the single quotes in the SQL queries.
            insert_query = insert_query_gen('form', ('', url, json.dumps(attributes), req_id, escape_quotes(
                form), method, action, absolute_action, param_ids))
            # print(insert_query)
            cursor.execute(insert_query)
            form_id = cursor.lastrowid
            # update and link the params to the form they were found in. Lets
            # us use the advantage of auto-increment without having to keep
            # track of it ourselves
            update_query = "UPDATE params SET form_id = %s WHERE id >= %s  and id <= %s" % (
                str(form_id), str(param_ids[0]), str(param_ids[len(param_ids)-1]))
            cursor.execute(update_query)
            db.commit()
            tasks = []
            row = (form_id, form)
            tasks.append(check_for_email_field.delay(row))


        except Exception as e:
            print("Definitely a database issue, well, hopefully. We are in form_parser")
            with open('log_form_parser', 'a') as file_handle:
                file_handle.write(str(e))
            print(e)
            return

    # print(req_id)
    # this return statement actually IS required for the queue to keep track
    # of state for next step in the pipeline, that is the check_for_email
    # step, only takes the form id and the content, remaining would just be
    # overhead and better stored in the db.
    # forget all the above, the return wont work, only one form will be returned,
    # not expected behaviour, so changed it
    # return str(form_id), escape_quotes(form)
