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
* call_email_form_retriever makes a db query to get the forms with email fields,
then reconstructs them into a proper ast structure, 
and then does a parallel pass to the celery queue.
* fuzzer then constructs the requests with the additional headers.
* The fuzzer has been split into multiple parts now, with malicious and non-malicious payloads.
* This is to save time on fuzzing only the forms that sent us emails in the first place.
* Also, the fuzzer uses a user_name that is set to (reg/mal/n)user followed by the form id.
* Have rerouted all such emails to 3 mailboxes using postfix :D

### Email Analyzer
* Thinking right about now (Jan 9) whether we need the E-Mail 
analyzer script, seeing as we are only going to nuke them with BCC.
* After discussion with the prof, a minimal email analyzer script 
that checks for x-dummy-headers, and bcc headers needs to be built.
* The mails in maluser are direct proof of the attack.
* But the mails in normaluser could contain the x-check
header, if they do, then that is a successful attack
as well. 
* This is due to pythons way of attaching
headers, instead of overwriting, it ignores duplicate
headers, so we need to inject a new one.
* So, for php, (and unduplicated python) we use the malusers file, 
for the duplicated headers, normaluser is checked.
* The reguser is checked to see which sites actually sent out emails :D, 
so that we can say, out of X sites, we got Y mails, out of which Z mails were fuzzed

### Test Suite
* Have written tests using Unittest module and mocks.
* Checks for all the fuzzer functions, and whether they behave correctly for all inputs.
* Added checks for all form_parser and check_for_email functions.
* NOTE: The tests are in python3, while the code has been down-ported
 to Python2 to ensure compatibility with the RabbitMQ queue :(
 So, comment out the Python2 specific lines before running tests --> This is a 
 LOT of work, but Python2 doesnt support the same Module structure as Python3, 
 so rewriting tests is also a pain

### To SSH:
ssh -p48064 sai@128.111.48.6
sudo ssh -p48064 -NL 5672:192.168.48.9:5672 sai@128.111.48.6 -v