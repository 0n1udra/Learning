import logging


"""
-Levels-
Logging Levels: Debug, Info, Warning, Error, Critical
0 for unset
10 Debug - Detailed info
20 Info - Confirmations or things working correctly
30 Warning - Smaller problem or warnings of possible future issues
40 Error - More serious issues, pats of program not working correctly
50 Critical - Crashes, bad errors
Default is Warning, Error and Critical

-Format-
%(message)s  --  The log message when calling .debug/info/etc()
%(asctime)s  --  Human readable time 2003-07-08 16:49:45,896
%(msecs)d  --  Millisecond
%(relativeCreated)d
%(created)f  --  time.time()  output
%(filename)s  --  Name of the file where log was called
%(lineno)d  --  Line number of where log call came from
%(module)s  --  Module name
%(funcName)s  --  Name of the function that contains that's logging
%(levelname)s  --  Level name, INFO, DEBUG, WARNING, etc
%(levelno)s  --  Logging level in numbers, 10-50
%(name)s  --  Name of the logger
%(pathname)s  --  Path of the file where log was called
%(process)d  --  Process ID
%(processName)s  --  Process name
%(thread)d  --  Thread ID
%(threadName)s  --  Thread name
Used in .basicConfig(format=" ")  separate each by something usually : well do, but you can use whatever, even mix it up if want
"""

l = logging.getLogger(__name__)
l.setLevel(10)

formatter = logging.Formatter("%(asctime)s:%(levelname)s|%(message)s")  # format

fileHandler = logging.FileHandler('Logging Info.log')  # file
fileHandler.setLevel(10)  # set level to only output x or higher
fileHandler.setFormatter(formatter)  # set the format for .log file

streamHandler = logging.StreamHandler()  # creates stream handler to show logging in the console
streamHandler.setFormatter(formatter)  # the format to show

l.addHandler(fileHandler)
l.addHandler(streamHandler)
# add the handlers



logging.basicConfig(filename='Logging Info.log', level=10, format="%(asctime)s:%(levelname)s|%(message)s")
# this sets the level where anything higher(the numbers) well be shown in run window
# l.basicConfig(level=10) well work too. so anything 10 or higher well be shown to console
# the filename=''  well put all the logging outputs to the file. Same as the console itself anything higher well be logged to file
# format sets the formatting of the log you want. you can't set these separably

def add(x, y): return x + y
def sub(x, y): return x - y
def mul(x, y): return x * y
def div(x, y): return x / y

n1 = 10
n2 = 5

addR = add(n1, n2)
l.debug("add: {} + {} = {}".format(n1, n2, addR))

subR = sub(n1, n2)
l.debug('sub: {} - {} = {}'.format(n1, n2, subR))

mulR = mul(n1, n2)
l.debug('mul: {} * {} = {}'.format(n1, n2, mulR))

divR = div(n1, n2)
l.debug('div: {} / {} = {}'.format(n1, n2, divR))


