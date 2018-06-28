# PyCharm


# Basics of Python

# 1. Data#		##########################################################################################################################################################
def basicData():
    # 1.1 variables
    string1 = "hi"  # makes a string with 'hi'
    int = 1  # makes a integer 1
    float = 3.14  # makes a float 3.14

    # a float is a decimal, a integer is a whole number
    answer = True  # a boolean, is a true or false variable
    replay = False
    nothing = None  # 'None' is an absance(blank) of data, because when making a variable you need somehting

    var1, var2, var3 = 1, 2, 3  # making multiple variables on one line, var1 goes to 1, var2 goes to 2 etc..
    print(int)


##### Naming ##############################################
# this is how I (Drake Thomas) would name things, everybody does it differently
"""
-Overview-
x, variable, thing = 12/'hi'/1.2
list2, dict1, namesOfPeople, foodToGet = []/{}/()
class Class, ClassOfStuff, ASimpleClass:
def func1/function_Does_Something/a_Quick_Func():

-Variables/lists/dict/etc-
integer = 12  --  one word
x = 12  --  should only use in enclosed loops, for global variables that you'll use a lot use comprehensive names
xy = 12
thingy = 'hi'  --  a quick variable you might not use a lot
sayHi = 'hello' --  something you might use a l ot
aVariableOfStuff = 'this is a variable' --  a very import variable that you'll call a lot and need to know what it is
list1 = []
aList = []
listWithData = []
aListOfNames = []
dict1 = {}
dictOfHomesAddrs = {}  -- a longer name. a dictionary of home addresses

-Functions-
def func1():  --  a quick function
def func_1():
def a_Function():
def function_That_Does_Stuff():  --   a important function that you might call a lot, or need to know what it does
def get_In_foFrom_Dict1():  --  function name that tells you what it does
def x():  --  should not use this. since it's usually a variable etc
function_var  --  all lowercase with _
-Class-
class Class1:  --  should be capitlized.
class Thingy_ThatDoes_Things:
class A_Quick_Class:
ClassVar  --  class variable, all uppercase, a class method var would be the same as a regular function name
Class_Function_Stuff()  --  a class function/method

-Other-
_obj  --  semi-private object
_function  --  this is usually used in a module file to hide the function, which means it's not meant to be used by the user, only the file. You can of course call the function but there's no point, only the file uses it
_var  --  same as the _function, this is suppose to be a hidden variable
__obj  --  super-private interpreter will usually do something with this
__name__  --  reserved for other python keywords/builtin/methods/attr/etc

"""


def printData():
    # 1.2 printing
    print("hi")  # prints text to console
    print("bye")  # prints 'bye' on a new-line

    print("hi " + "\nbye")  # prints 'hi' 'bye' on separated lines, like the two prints above just on one line

    print("yo", 1)  # prints 'yo' and then 1, the ',' is to print other stuff
    print("yo " + "hey")  # concatenates the two words, you need to add spaces in the string so it doesn't run on

    print('lol' * 10)  # prints out string 10 times

    print('1'), print('2')
    # using two print statements on the same line, but it doesn't actully print 1 and two on same line
    # you can usually do multiple things on the same line, sometimes not. Experiment


def lTSD():
    # list, tuple, set, dictionary

    # 1.3 lists, tuples, sets, and dictionaries
    list1 = [1, 2, 3, 'hi', 'bye']  # makes a list 'list1' (editable)
    list2 = [1, 2, 3, [4, 5, [6, 7], 8], 9]  # nested lists
    # a list in a list well be treated as one item when calling.
    # e.g. print(list[3]) this well print out all of the in the nested list that was made in position 4 >
    # [4,5,[6,7],8]

    list1.append('goodbye')  # adds 'goodbye' to the end of list1
    list1.pop(1)  # removes 1 from list1

    print('list1:', list1[1:3])  # prints items 2 - 4, :2, 5:, :, -3:, :-3
    print('list2', list2[4][1])
    # this well print out 5, since you call the list at index 4 and then the item in the list at index 1

    # Tuples
    tuple1 = (4, 5, 6, "foo", "bar")  # makes a tuple 'tuple1' (non-editiable)
    # you can't edit tuples

    # Sets
    set1 = {1, 1, 2, 2, 3, 3, 3, 'four', 'four', 'five', 'five'}
    # same as a list but it takes out duplicates
    print('set1:', set1)  # prints out set

    # Dictionaries
    dictionary1 = {'name': 'Drake', 'age': 15, 'home': 'sandown'}  # makes a dictonary 'dictonary1' (editable)
    # 'name' corresponds to 'Drake', 'age' corresponds to 15.....etc..
    dictionary1['planet'] = 'earth'  # adds entry 'planet' and value as 'earch'
    del dictionary1['home']  # deletes item from dictionary
    print('dictionary:', dictionary1['name'])  # prints name from dictionary1
    # for looping through all of the items go down to looping


def convertData():
    # conversion
    toConvert = [1, 1, 2, 3, 3, 'four', 'five', 'six', 'six', 'six']
    newTuple = tuple(toConvert)  # converts list to a tuple ()
    newSet = set(toTuple)  # converts to a set {}
    newList = list(toConvert)  # converts to list []

    toDict = [['one', 1], [2, 'two'], [3, 3]]  # a nested list
    newDict = dict(toDict)  # the nested items first item well be the key.
    # e.g.  {'one':1, 2:'two', 3:3}


# 2. statements, functions#		##########################################################################################################################################################

def ifElifElse():
    # 2.1 if/elif/else
    print('if/elif/else.........................')
    y = 1
    if y == 1:  # checks if y = 1
        print('1')
    elif y == 2:  # checks if y = 2
        print('2')
    else:  # if y not equal 1 or 2, does this
        print('3')
    # don't need elif, it just adds more options
    print("2.1 if/else/elif .....................................")

    # 2.2 try/except/finally
    print('try/except/finally...........................')
    inp = input("Input number: ")
    try:
        inp = int(inp)  # tries to convert to integer
        print(inp)
    except:  # if the try part fails, then this runs
        # you can have multiple except statments. to catch different errors. lookup exception errors for errors to print out
        print('not a integer!')  # if fails does this
    else:
        print('um')
    finally:  # runs at end, whether it faild or not
        print("done")
    # usually don't need finally

    try:
        pass  # code
    except ValueError:
        pass  # if exception is ValueError..
    else:
        pass  # if it's anything else then...


def functions():
    # 2.3 functions
    def adding(num1, num2):  # defines(makes) a function called adding, with paremeters 'num1','num2'
        sum = num1 + num2  # whatever you input this adds them together and puts it in 'sum'
        return sum  # returns the value of sum, becuase a function is closed off. As in outside data can't be read from inside the function and outside can't read data from within function, unless you use global or return.

    # returns 10, not print to print it >
    print(adding(5, 5))


def classes():
    # 2.4 class
    class Class1:
        def __init__(self):
            self.printHi()  # when class is called, this runs, and can call any other functions from later on in the class

        def printHi(self):
            print('Class1:', "hi")

        def printBye(self):
            print('Class1:', "bye")

    newInstance = Class1


# creates a new instance of a class, since you have a __init__ method that well run when a new instance is made

def basicListMethods():
    # 2.5 built in functions/methods
    Numbers = [2, 5, 46, 74, 3, 6, 3, 6, -3, 6, 3, 6, 2, 21, 34, 6, 8, 6, 3, 533, 34725, -12,
               -15, -15, 2]  # makes a list of numbers to play with
    # this works with tuples too
    print('min: ', min(Numbers))  # prints the minimum number in the list
    print('max: ', max(Numbers))  # prints the maximum number in the list
    print('abs: ', abs(Numbers[8]))  # prints the absolute value for the number
    print('type:', type(Numbers))  # prints what 'Numbers' is, which is list object
    print('list: ', list(Numbers))  # makes into list. but already a list
    print('tuple: ', tuple(Numbers))  # makes into tuple, similar to list main difference not editable
    print("sorted: ", sorted(
        Numbers))  # sorts the data, numbers lowest to highest(lowest negative then highest positive, -10, 1), works with letters to a-z, A-Z, etc
    print('set: ', sorted(set(
        Numbers)))  # makes set, similar to tuple but removes duplicates. there's also a sorted method on it. so it converts to set then sorts
    numDict = {k: v for k, v in zip(range(len(Numbers)), Numbers)}  # creates a dictionary, zip(keys, values)
    print('numDict: ', numDict)


# basic python methods for lists

def compareing():
    # 2.6 comparators and, not, or
    var1 = 1
    var2 = 2
    var3 = 3
    if var1 and var2 == 1:  # checks to see if 'var1' and 'var2' is 1, if one of them is not 1 then it returns false, and doen't run the code. both have to be 1
        print('both are equal to one')
    elif var2 or var3 == 2:  # if one of the var(s) is equal to 2, then it runs the code
        print("one of them is 2")
    elif not var3 == 3:  # if 'var3' not equal to 3 then is runs the code, if it does it skips
        print("var3 is not 3")
    else:
        pass  # pass does nothing, just skips


# python comparing statments

def breakContinue():
    # 2.7 break, continue
    for n in range(2, 10):  # runs through the numbers 2-10
        for x in range(2, n):  # runs through the number 2-n (8)
            if n % x == 0:  # checks to see if n % x has no remienders
                print(n, 'equals', x, '*', n // x)
                break
        else:
            # loop fell through without finding a factor
            print(n, 'is a prime number')  # if so then prints this

    print("2.7 break......")
    for num in range(2, 10):
        if num % 2 == 0:
            print("Found an even number", num)
            continue
        print("Found a number", num)


# break/continue keywords for skipping a loop or stopping

# 3. looping#		##########################################################################################################################################################
def looping():
    # 3.1 while loop
    x = 0
    while x < 5:
        print("whatup")
        x += 1
    else:
        print("done")

    # you can also add a else statement at the end if want to(doesn't need an else)
    # 3.2 function loop with for
    def whatup2():
        print("whatup2")

    print("3.2 looping. function .......................................")

    # 3.3 makes for loop to call function that prints 'whatup2'
    for i in range(5):
        whatup2()
    # calling the function 5 times
    print("3.3 looping function ...............................")

    # 3.4 for loop
    for i in range(5):
        print(i)

    # Dictionary looping
    dictToLoop = {1: 1, 'two': 2, 3: 'three', 'four': 'four'}
    for k, v in dictToLoop.items(): print('key:', k, ':: Value:', v)
    # counts down from 5 and prints it out

    x = [1, 2, 3, 4, 5]
    for i in x:
        print(i)
    else:
        print('Done')

    for i in x:
        print(i)
        if i == 3: break
    else:
        print('done')

    def find(list, target):
        for i, item in enumerate(list):  # runs through list
            if item == target: break  # if i == target it breaks the loop
        else:
            return -1  # if break was not called, it'll return -1, which means not in list
        return i  # if break is called then it'll return, which is the position in list where it stopped becuase the break

    names = ['Kirby', 'Drake', 'Emoji', 'Shades', 'Thing']
    index = find(names, 'Shades')
    print("Shades at index {} in names".format(index))


# Looping, while loop, for loop

def dictionaries():
    pass


# dictionary
def strings():
    person = ['Kirby', 10, 'Pink', 'Cute', 'Cake']

    # the S| , S3.1| repeat| is to track what corresponds with what in the code, since this prints a lot, S is sentence if you couldn't guess :-)
    sentence = "S| Hello I'm " + person[0] + ", I am " + str(person[1]) + " years old, I'm " + person[2] + ", also " + \
               person[3] + ". My favorite food is " + person[4]
    # not the bst way to print something like this out. It's hard to read, to keep track of what variable your getting, and it's somewhat long(not the sentence, it's how you wrote the format)
    print(sentence)

    sentence2 = "S2| Hello I'm {}, I am {} years old, I'm {}, also {}. My favorite food is {}.".format(person[0],
                                                                                                       person[1],
                                                                                                       person[2],
                                                                                                       person[3],
                                                                                                       person[4])
    # in the " " use {} to use as a place-holder, then .format to tell what to put in the place holder. it'll put the corresponding data according to start-end positioning
    # this is much easier to read; since you do't have the "" cut of every other part. but it's still long.
    # you can also see here with person[1] which is a integer; we didn't need to convert that into a string from .format()
    print(sentence2)

    # --- Specify position ---
    sentence2_1 = "S2.1| Hello I'm {4}, I am {0} years old, I'm {3}, also {1}. My favorite food is {2}.".format(
        person[0], person[1], person[2], person[3], person[4])
    # it looks similar to the one above, but here you can specify what data corresponds to what. In the .format() {0} would be the index of 0 in .format() duh. no you cannot change this
    # this works with dictionaries and tuples, with dictionaries you'll use the key instead, duh
    print(sentence2_1)

    # --- Repeating same data ---
    # the {1} specifying what corresponds to what is most useful if you have to repeat something, Ex.
    repeat = 'repeat| {0} is my favorite, {0} is yummy, {0} is awesome, {1} is ok but {0} is better!'.format("Cake",
                                                                                                             "Cupcake")
    # as you can see you can call again the place-holder multiple times
    print(repeat)

    # --- Grab within {} ---
    sentence3 = "S3| {0[0]} is here, {0[0]} is Ready!. {0[4]} is my favorite!".format(person)
    # here you can see that we can get data from the list from right in the {} place-holder chars, and we can repeat the {0} like from above,
    # this would be the same as > sentence3 = "{0} is here, {0} is Ready!. {1} is my favorite!".format(person[0], person[4]) . but this way we need two args in .format(), the above one we don't
    print(sentence3)

    # the {} works with class obj too, you need a class instance first, (inst = Class()) . then you can call that class object like how you would regularly >
    # sentence = "hi {}".format(inst.name) , or sentence = "hi {0.name}".format(inst)
    # you cannot just call the intire object/var/etc from with {} in "", e.g. s = "Hi {inst.name}".format() This won't work, nor well it work for variables s = "Hi {x}".format(), and no removing the .format() won't change anything

    # --- args ---
    sentence3_1 = "S3.1| {name} is here, {name} is Ready!. {food} is my favorite!".format(name="Kirby", food="Cake")
    # this well match up the names fro within {} with the args from the .format(), so {name} well be "kirby" since in .format(name="kirby")
    print(sentence3_1)

    # --- With Dict ---
    aboutPerson = {'name': 'Kirby', 'food': 'Cake', 'mood': 'happy'}  # creates dictionary about person
    sentence3_2 = "S3.2| {name} is here, {name} is Ready!. {food} is my favorite! I'm {mood} right now.".format(
        **aboutPerson)
    # the **aboutPerson in .format() is unpacking all the data from the dict, then in the {} you call the key from dict. Seems very useful
    print(sentence3_2)

    # --- {} Padding and Numbers---
    for i in range(0, 11): print("Numbers: {:02}".format(i))
    # this well only show 0 before single digit numbers. e.g. 01, 02, 03 .... 09, 10, 11
    # if you did {:03} then it'll be 001, 002, 003 .... 009, 010, 011 ... 099, 100, 110  , and so on

    print("Comma Number|{:,}".format(1000 ** 2))  # 1000**2 = 1,000,000
    # the {:,} well add a comma to seperate the section so it's more human readable instead of just 1000000 > 1,000,000  . it won't work with everything e.g. {:.} won't work >
    # what well work {:,} ,/_/+  . the + well um

    print("Decimal Number| {:.2f}".format(3.14159265359))
    # {:.2f} well only show 2 numbers after the decimal . . the f is for float
    # so {:.5f} would be 3.14159

    # ----- Datetime -----
    # Date = dt.datetime(2017, 3, 15, 11, 35, 55) # sets date and time. Year, Month, Day, Hour, Minute, Second
    # you can input your own data like above, put i'm going to use the current relavent date and time
    Date = dt.datetime.now()
    print("Datetime|", Date)  # prints out date and time in this format Y-M-D H:M:S

    print("Datetime Formatted| {:%B %d %Y, %X}".format(Date))  # formats the date as specified,
    # common ones to use. Month  -- %B - full month name (January) %b small Month name (Jan), %j - the day number of the year (50 or 360)
    # Day  --  %d - day of moth, %A full Day name(Monday), %a shortened Day name(Mon)
    # Year  --  %Y - full year (2017), %y - shortened year (17)
    # Time  --  %X - Time (11:35:55), %H - 24h Hour, %I - 12h Hour, %M - Minutes, %S, Seconds
    # All  --  %c everything (Wed Mar 15 11:35:55 2017), %x - date (03/15/17),

    print(
        "Datetime Formatted with text| Today is {0:%A} on {0:%B %d}, the {0:%j} day of the year. And the time is {0:%X}".format(
            Date))
    # you can add text and move the data around like this to give a full sentence with the date and time. you do need the 0 part in {0:%j}, since that says get data from Date

    # go to small modules.py for more on datetime


# better print output, and more complex concepts
basicMethods()

"""
~False               ~def                 ~if                  raise
~None                del                 ~import              ~return
True                ~elif                ~in                  ~try
~and                 ~else                is                  ~while
as                  ~except              lambda              with
assert              finally             nonlocal            yield
break               ~for                 ~not
~class               from                ~or
continue            ~global              ~pass

"""
