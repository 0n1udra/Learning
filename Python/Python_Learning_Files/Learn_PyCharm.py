# read this file to learn more about PyCharm IDE

"""
PyCharm file highlight coloring
Black - up to date, unchanged
Gray - deleted
Blue - file has changed, file changed since last sync
Green - new file, file need to add to repo
Violet - merged, file has been merged by VCS from update
Brown - unknown, file local but not on repo and not scheduled to be added
Olive - file well be ignored in any VCS operations
Light Brown - hijacked
Red - merge conflict from last sync
Lilac - deleted locally, not scheduled to be deleted in CVS repo
Dark Cyan - moved to another brance

----- Useful Stuff -----
Enable all of PEP8 to Warnings in inspection
hold option/alt and click other places to have multiple cursors, to type multiple lines at once!
double press option/alt then use arrows to add more cursors
hold ctrl then use arrows to go through open tabs
hold command/..  while pressing enter to create new line in the code but without cursor moving
use inspect code to find errors, redundant things, spelling, and PEP guidelines. works on directories too.
use the favorites panel.®®®®
---
TODO: ...  --  start comment with this to add to todo list. access from TODO panel


----- Shortcuts -----
command+s  --  save file
shift+command+ -/+  --  collapse or expand all
command+ -/+  --  while in method of some sort collapse or expand
while cursor on error/problem alt+enter  --  show suggestion for fix
double alt + arrows  --  make multiple cursors
hold down alt then mouse  --  place multi cursors
command+/  --  comment code, works with multi line highlight
control+space  --  bring up autocomplete help
command+ctrl+l  --  reformat code, fixed to PEP8(as of 2017) standards
"""


# TODO: HEY THERE

# Text color text/example

string = 'HI  h I hh  yal' # # text
integer = 12 # integer
boolean = False # boolean
float = 1.5 # float
list1 = [1,2,3] # list
tuple1 = (1,2,3) # tuple
dict1 = {1:'one', 'two':2, 3:3, 'four':'four'} # dictionary
set1 = {1,2,3,3,2,1,1,2,3,1,2} # set

toConvert = 99
toString = str(toConvert) # convert to string
toList = list(toConvert) # convert to list
toTuple = tuple(toConvert) # to a tuple
toSet = set(toConvert) # to a set

mathStuff = 1 + 2 - 3 / 4 * 5 ** 6 + (1 // 2) - 5 % 2
# add, subtract, multiply, exponent, parentheses with floor devision, modulo

print("Hello"+"World") # print statement with concatenated string
print('how\'s it \tgoing\n') # print statement with \' \t - tab \n - newline
print("PyCharm", 'is the best', string) # print statement with multiple strings and variable

def func_1(params, *args): print("A Basic funcgion", params, *args)
# a basisc function with parameters
func_1('hello', 'uh') # call function with input

lambdaFunc1 = lambda someInput: print(someInput) # lambda function
lambdaFunc1('input')

if not 1 == 1: print("ok") # if statement, if 1 does NOT equal 1
elif 1 % 3 == 0 and 1 // 4 == 2: print("um") # if 1 divided by 3 is 0 or 1 // 4 is 2
elif 1 <= 5 or 1 >= 6: print("mhm") # if 1 is smaller or equals 5, or 1 is bigger or equals 6
else: print("nope") # else

counter = 10
while counter > 0:  # while loop, stops when counter hits 0
    print("bigger then zero")
    counter -= 1 # subtracts one from counter every loop until 0

var = 'outside variable 1'
class aClass:
    var = 'class variable 1' # class variable
    def __init__(self, something): # class __init__ function
        self.something = something # instance variable
        self.classFunc() # call class function

    def classFunc(self): print("HI from a class")
        # class instance function

    @staticmethod
    def staticMethod(): pass

    @classmethod
    def classMethod(cls): print(cls.var, var)

callClass = aClass('inputted something')
print(callClass.var) # print class variable

for i in range(10): print(i) # for loop, loops through 9 times


#https://www.geeksforgeeks.org/python-docstrings/
#https://stackoverflow.com/questions/3898572/what-is-the-standard-python-docstring-format
#http://sphinxcontrib-napoleon.readthedocs.io/en/latest/example_google.html
def googleDocString(param1, param2):
    """
    This is an example of Google style.

    Args:
        param1: This is the first param.
        param2: This is a second param.

    Returns:
        This is a description of what is returned.

    Raises:
        KeyError: Raises an exception.
    """

def numpyDocStr(array_like, second_Param):
    """
    My numpydoc description of a kind
    of very exhautive numpydoc format docstring.

    Parameters
    ----------
    first : array_like
        the 1st param name `first`
    second : second_Param
        the 2nd param
    third : {'value', 'other'}, optional
        the 3rd param, by default 'value'

    Returns
    -------
    string
        a value in a string

    Raises
    ------
    KeyError
        when a key error
    OtherError
        when an other error
    """

def reSTDocStr():
    """
    This is a reST style.

    :param param1: this is a first param
    :param param2: this is a second param
    :returns: this is a description of what is returned
    :raises keyError: raises an exception
    """

def epytextDocStr():
    """
    This is a javadoc style.

    @param param1: this is a first param
    @param param2: this is a second param
    @return: this is a description of what is returned
    @raise keyError: raises an exception
    """




