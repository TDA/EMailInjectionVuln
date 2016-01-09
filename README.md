## Email Header Injection Vulnerability Project

Note: Starting point is call_form_parser.py, please check 
that file, everything from there is marked in the comments.

*Note to self:* If you ever write another project in Python3 without EXPLICITLY
specifying it, then I will kick you myself, however improbable that may sound. 
EIBTI !!! remember that, at least in Python :D :D

### Crawler
1.  CeleryCrawler.py is the config file (kinda), and sets up the queue to execute.
2.  The call_for_ scripts are basically built to use with Celery, 
they use the .delay() method to add the tasks asynchronously.
3.  functions.py is a general purpose library written for this project, 
but can definitely be reused with other projects.
4.  form_parser and check_for_email are the backbone scripts of this Crawler, 
they parse the forms and pull up the forms that have email fields respectively.

### Fuzzer


### Email Analyzer
* Thinking right about now (Jan 9) whether we need the E-Mail 
analyzer script, seeing as we are only going to nuke them with BCC.