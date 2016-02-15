## Email Header Injection Vulnerability Project

Note: Starting point is call_form_parser.py, please check 
that file, everything from there is marked in the comments.

*Note to self:* If you ever write another project in Python3 without EXPLICITLY
specifying it, then I will kick you myself, however improbable that may sound. 
EIBTI !!! remember that, at least in Python :D :D

*Note to self:* Had to downport to Python2, so this entire thing was rewritten :(

### Crawler
1.  CeleryCrawler.py is the config file (kinda), and sets up the queue to execute.
2.  The call_for_ scripts are basically built to use with Celery, 
they use the .delay() method to add the tasks asynchronously.
3.  functions.py is a general purpose library written for this project, 
but can definitely be reused with other projects.
4.  form_parser and check_for_email are the backbone scripts of this Crawler, 
they parse the forms and pull up the forms that have email fields respectively.
5.  Start the crawler like so,
        python CeleryCrawler.py worker -l INFO
6.  And then run the parser, like so
        python call_form_parser.py

### Fuzzer
1. call_email_form_retriever makes a db query to get the forms with email fields,
then reconstucts them into a proper ast structure, 
and then does a parallel pass to the celery queue.
2. fuzzer then constructs the requests with the additional headers. 

### Email Analyzer
* Thinking right about now (Jan 9) whether we need the E-Mail 
analyzer script, seeing as we are only going to nuke them with BCC.
* After discussion with the prof, a minimal email analyzer script 
that checks for x-dummy-headers, and bcc headers needs to be built.

### Test Suite
* Have written tests using Unittest module and mocks.
* Checks for all the fuzzer functions, and whether they behave correctly for all inputs.
* Added checks for all form_parser and check_for_email functions.

### To SSH:
ssh -p48064 sai@128.111.48.6