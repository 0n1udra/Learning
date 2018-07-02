import os
import sys
import random
import time
import datetime as dt
import collections as cl


def Cache():

    a = time.time()

    funcCache = {}
    # this well be the cache of the function

    def aFunc(x):
        if x in funcCache:
        # checks if x is already in the cache, if so returns the item that's in the cache dict
            return funcCache[x]
        else:
            result = x * x + x / x ** x + x  # does stuff
            funcCache[x] = result  # adds result to the dictionary with key x
            print("Computing:", x)
            time.sleep(1)  # pauses, to make it seem like it's doing stuff
            return result

    print(aFunc(1))
    print(aFunc(2))
    print(aFunc(3))
    print(aFunc(4))
    print(aFunc(4))
    print(aFunc(5))
    print(aFunc(3))
    print(aFunc(1))
    print(aFunc(6))
    print(aFunc(8))
    # ten print statements, probably could'v done better

    print("Took:", time.time() - a)  # prints out how long code took to run

    # in the end this should take about 7s, it would'v been 10 if we didn't use the cache
# Memoization and Caching

# uses datetime as dt

def string_Slicing():
    x = 'http://www.lolollolololhaha.com'
    # a website address

    print("http :: ", x[:7])
    # this well get the http:// part. [:7] means get everything and stop at 7
    print("Domain :: ", x[-4:])
    # this well get the .com part. [-4:] means get everything from the last 4
    print("Site :: ", x[7:-4])
    # this is the main site the www.site . [7:-4] means start at 7 end at -4
# basic string slicing

def time_Code():
    # time code execution

    A = time.time()
    # do stuff
    print('hi')
    B = time.time()
    print('Time: ', A - B)
# time the code execution

def no_Errors():
    # buts any errors you get into a null class, basically you won't get any.
    class DevNull(self, msg):
        pass
    sys.stderr = DevNull()
    #you can comment out 'sys.stderr = DevNull()' part to show errors.
#  hides error, should not do this when you need to know what went wrong. DUH!

def have_Spaces():
    # if your making a real and big program, have it readable and beautiful, especially when teaching; make it READABLE.
    # if your making a quick and test program or to show a concept, you can make it more compact to save space.

    for i in range(5):
        print(i)
    # compact version
    for i in range(5): print(i)

    x = 0

    # this can work for most things with ':' at end
    if x == 1: print('one')
    else: exit()
    # should only use this when using small command after, so it's still easy to read, unlike this >
    if x == 2: print(x+1), print(x+3), exit()
    # space your code out so it's more readable, unless it's something really small or it's a test/example file. on a real program have it readable for other people and yourself later on.

    # this is still kinda readable. you can't use the shortl format if you have more then one command sometimes e.g. >
    num = 50
    if num > 10: print("bigger then 10")
    elif num < 100: print("smaller tehn 100")
    elif num == 777: print("Num = 777")
    else: print("I don't know what num is")

    # But really should be like this
    if num > 10:
        print("bigger then 10")
    elif num < 100:
        print("smaller tehn 100")
    elif num == 777:
        print("Num = 777")
    else:
        print("I don't know what num is")


def making_Mods():
    # modules

    def func1(): print('This is a function!!')
    # you would put this in a another file
    # then in main file use import
    # import functions or from functions import *
# making your own module


# ===== File I/O =====

def file_IO():
    FILE = 'testfile.txt'
    NL = '\n----------'
    openFile = open(FILE,"r") # opens file to read, you can put in the path or name of the file in "" as the first arg, but for ease I putted that in a var
    # opens the file, 'r' means read file
    #"r" - read,  "r+" - read and write,  "w" - write,  "a" - append,  "b" - binary

    openFileContents = openFile.read()
    # this well read the file. the 'r' in the open() doesn't mean it'll actually read the file, that just means what are you going to do with the file
    print("from openFile, using open():")
    print(openFileContents) # prints contents of the file, as the way the file was types/etc (lines/tabs/etc well show up)

    openFile.close() # you should always use .close when using x = open()

    print(NL, 'withOpenFile:')
    # ----------
    print("from withOpenFile, using with open():")
    with open(FILE, 'r') as withOpenFile:
    # this well open the file for just this code then closes it after the code has finished. This is a easier way then just x = open() >
    # but the advantage to the other way is that you can keep the file open to call to it later one, but then again you would probably open the file; put the needed data into a list or a array of somekind, then close it....
        withOpenFileContents = withOpenFile.read()
        print(withOpenFileContents)

    # you could just use .read() right when you open the file, Ex. x = open("file", 'r').read()  or  with open("file", 'r').read() as f:
    # the .read() loads the whole file into memory; if you do x = read() (same goes for the other (.readlines()),

    # ----------
    print(NL, "f:")
    with open(FILE,'r') as f:
        print(f.readlines()) # this well return all of the data in list, separated by new lines
        # the list well show the \n chars and any others also, this well store the file data in memory also; since it puts it in a list. in this case i'm just printing it, but you can do x = readlines()
        print(f.readline()) # this well just show one line from file
        # this won't work since we already have f.readlines()

    # ----------
    print(NL,"f2:")
    with open(FILE, 'r') as f2:
        for line in f2: print(line, end='')
        # since your not declaring a new variable, x = read()  , this well only print out the data from file, and not store it

    # ----------
    print(NL, 'f3:')
    with open(FILE, 'r') as f3:
        f3Contents = f3.read(50)
        # this specifies only read 100 chars from file, this does save it to memory, you can use print(f3.read(100)) if you don't want to save to mem
        print("50 Chars:", f3Contents)

        print(f3.tell()) # this well print the position of what position it is in file by chars, since we have the .read(100) this should return 100
        f3.seek(100) # this well move the position of where to start reading from, .seek(0) would be the beginning of the file
        print("moved to:", f3.tell()) # print the position again
        f3Seeked = f3.read(20)
        print("20 more chars:",f3Seeked) # print out 20 more chars

        print("f3 writable: ", f3.writable()) # prints if file is writable. This doesn't return whether the actual file is writable, only if this script can
        print("f3 readable: ", f3.readable()) # prints whether you can read the file in the script, not whether the computer can

        print(f3.closed) # prints boolean of whether it's closed or not, closed = True
    print(f3.closed) # this well return true; since this is outside the with open(), which means it did closed

    # ----------
    print(NL, 'f4')
    with open('testFile2.txt', 'w') as f4:
        # the 'w' well create a testFile.txt if it doesn't exist, if it does it'll overwrite it with a new one(if this script has that permission), So be-careful that so you don't overwrite important files
        # use 'a' or 'r+' if you want to add to file without overwriting it, you can use 'w' if you want to make a new fil and add things to it. This does work with the x = open() way
        print("Created testFile2.txt")
        f4.write("Hello World!") # write data to file
        print("Wrote 'Hello World! to file")
        f4.seek(0)
        f4.write("Bye") # be-carful with this also, beacuse this well overwrite data if something is already at the position, it won't delete the whole word if there is one; it'll only overwrite what it needs to to write out the new data
        print("Wrote Bye at beginning of file")

    # ----------
    print(NL, 'rf and wf. Copying files.')
    with open(FILE, 'r') as rf:
    # opens File to be read
        with open('copy_Of_testFile.txt', 'w') as wf:
        # creates copy_Of_testFile.txt , overwrites it if it already exists. you can make a if/else to check if it already exists with os or try/except
            wf.write(rf.read())
            # gets data from rf and puts it in wf, overwrites it if it already exists, but with the 'w' in with open() the file well be overwritten with a blank one anyway, you can also use a if/else to check if each line exists already

        print("Copying testFile data to copy_Of_testfile")
        print("Done...")

    # ----------
    print(NL, "rf2 and wf2. copying images" )
    with open('Kirby.png', 'rb') as rf2:
    # opens image and reads binary data
        with open('Kirby_Copy.png', 'wb') as wf2:
        # creates a file with name Kirby_Copy.png and well write to it by binary
            wf2.write(rf2.read())
            # copys every binary data from Kirby.png to Kirby_Copy.png

        print("Making copy of Kirby.jpg")
        print("Done...")
# file reading/editing and more

def read_File():
    f = open("FILE.txt", 'r').read() # opens file and reads it
    for line in f.split('\n'): print(line)
    # loops through f and splits it by new line, then prints that line

    with open("FILE.txt", 'r') as f:
        for line in f: print(line)
        # does the same thing. opens file loops through and prints each line
        # then it closes file after the code is done. you can also see that you didn't need the .read()
        # do not that if you don't specify .split('\n') it well show newlines between every loop,
# read lines from file


# ===== vars/lists/dicts/tuples/sets/etc =====

def setting_Sets():
    groceries = {'cereal','cereal','milk','milk'}
    # creates a set
    print(groceries) # prints set
# sets

def zipping():
    first = ['bob','bill','tom','taylor','rachel','um']
    last = ['thomas','carman','hanks','swift','nichols','oh']
    names = zip(first, last)
    for a,b in names: print(a,b)
# using zip()

def lists_Basics():
    x = 'hi - Kirby - how are you doing? - bye' # a string
    greeting, name, question, bye = x.split('-')
    # splits string by dashes then puts into a list for each item, then assigns that item from list to the corresponding variable >
    # so greeting = hi , name = Kirby , etc.....
    print(question)

    list1 = [1,2,3,4,5,1,2,6,2,3,2,6,2,5,7,9,3,5,10,11]
    print(list1)
    print('len:', len(list1))
    # prints the length of the list, in other words how many items in it
    print('max:', max(list1))
    # finds the largest item in the list
    # this doesn't work very well with letters, if there are letters it chooses the highest letter by alphabet. and if there are a mix of letters and numbers, it'll probably crash
    print('min:', min(list1))
    # prints smallest item in list
    print('count(2):', list1.count(2))
    # shows how many times an item appears in the list, works with strings and vars

    print('sum:', sum(list1))
    # prints the sum of a list. Does NOT work with: strings, vars, mixed, and muiti dimensional lists

    list1[0] = 12
    # changes first item in list1 to 12
    print(list1)
    del list1[1]
    # deletes item from list

    list1_item = list1.pop(0)
    # takes first item from list1 and removes it from list1 and puts it in list1_item var
    print('list1_item:', list1_item)
    list1.remove(1)
    # removes 2nd item from list1
    print(list1)
    numDict = {k:v for k,v in zip(range(len(list1)), list1)}
    # creates a dictionary of list1 with the keys as ascending numbers
    # go to Advance for more coplex list comprehension and more
    print('numDict:', numDict)

    ### String Meothods ###
    Str1 = 'Hello World, how ya doin!'
    Str2 = 'Hi, WTF, YO, uh, oooh, JULY 28!'
    print('Str1:', Str1)
    print('Str2:', Str2)

    print("Str1.split(' '):", Str1.split(' '))
    print("Str2.split(',':", Str2.split(','))
    # splits string into list items from .split arg
    print("' '.join(Str1):", ''.join(Str1))
# more on lists

def mutable_Immutable():
    a = 'hi'
    # strings are immutable, as in it can't be changed or edited. THAT DOESN'T mean it can't be overwritten >
    print(a, ':at:', id(a))

    a = 'bye'
    # this works because your not changing a your basically deleting a and making a new one
    # to see that happen these print statements show a's memory id(memory location). you'll see it change since Python deleted a then made a new one
    print(a, ':at:', id(a))
    # a[0] = 'b'  This well not work since this is trying to change a letter in a

    b = [1, 2, 3, 4, 5]
    # list are mutable, so you can edit the list or an item or multiple items at once etc
    print(b, ':at:', id(b))

    b[0] = 9
    # this changes an item at position 0(the first item)
    # but the memory location doesn't change, since it's the same list but one item has been updated
    print(b, ':at:', id(b))


    """
    Mutable:
    Lists []
    Dictionaries {}

    Immutable:
    Strings ""
    Integers 1-9
    Booleans True/False
    Tuples ()

    A reason why you might want to use a immutable object (tuple) vs a mutable one (tuple) is for the performance.

    """
# Learn about mutable/immutable datatypes

def variable_Comprehension():
    atHome = True
    say = "You're at home" if atHome else "You're not home"
    # say variable well be different if atHome is True or False
    print(say)

    # same as....
    atHome2 = False
    if atHome2:
        say = "You're at home"
    else:
        say = "You're not at home"
    print(say)
# kinda like list comprehension but with lists, this just shows if/else

def number_List():
    list = ['hi','bob','item','um','hmmmm','mhmmmm']
    # a new list

    for n, i in enumerate(list):
        print(n, i)
    # enumerate creates a tuple with each item with number order. e.g.
    # [(1,'hi'),(2,'bob'),(3,'item'), etc,etc). and the loop prints each item out


    # not the best way >
    for i2 in range(len(list)):
        print(i2, list[i2])
    # this just gets len of list, and i2 is the position of item(index) and prints out the position(index) number with the corresponding item
# ways to number your list items, use enumerate

# ----- Dictionaries -----
def get_From_Dict():
    dict = {'person1':1,
            'person2':2,
            'person3':3}


    # if else way
    if 'person4' in dict: person4 = dict['person4']
    # this checks if person4 is in dict, if so it puts that value in person4 variable
    else: person4 = 'not in there'
    # if not then person4 variable is this text

    # quicker, easier way
    person4 = dict.get('person4', 'not in there')
    # this checks if person4 is in dict if so puts in variable if not then it falls back on the second argument

    print("Person4:", person4)
    # prints value of person4
# check if item is in a dict or not

def twoList_OneDict():
    names = ['kirby','emoji','rhino','brain','smiley']
    colors = ['pink','yellow','blue','gray','red']
    # two lists with items


    nameColor = dict(zip(names, colors))
    # makes a dictionary from zip(). items from names well be the key, and color well be the values
    print(nameColor)


    d = {} # blank dictionary
    for aName, aColor in zip(names, colors):
    # zips items together to put into aName and aColor
        d[aName.capitalize()] = aColor
        # then adds to dictionary, but the keys well be capitalized
    print(d)

    # does the same as above, puts items from two lists into a dictionary and capitalizes keys
    d2 = {aName.capitalize(): aColor for aName, aColor in zip(names, colors)}
    print(d2)

    # with all of these the items well be in different orders every time you run them
    # continue to next function to learn more
# dictionary comprehension, and for loops with two lists

#uses collections as cl
def more_Dictionaries():
    dict1 = {"Kirby":1,
             "Smiley":1,
             "Emoji":1,
    }
    # creates a dictionary

    #####

    if 'Keeby' in dict1: # checks if 'Keeby' is in dictionary
        number = dict1['Keeby'] # if so puts the value in number
    else: number = 0 # if not then number = 0

    #####

    number2 = dict1.get("Keeby", 0)
    # a quicker version of above if/else. checks if 'Keeby' is in dictionary, -
    # if so number2 = the value from dictionary. if not then number2 = 0

    #####

    dict2 = cl.defaultdict(lambda: 'Not in Dict')
    # creates a blank dictionary, if you call an item thats not in the this dictionary it'll return a default value, which is 'Not in Dict'
    dict2.update(dict1)
    # puts all of the data from dict1 into this one

    print("How many Keeby's:", dict2['Keeby'])
    # print out how many Keeyb's, since Keeby is not in the dict it'll printout the default value 'Not in Dict'
    print("How many Kirby's:", dict2["Kirby"])
    # prints out how many Kirby's, since Kirby is in Dict it'll print out the value 1 from, since dict2 has the same data from dict1

def dict_Looping():
    classmates = {'tom':'decent person', 'bob':'smelly but not cool', 'charlie':'cool drug dealer'}
    # new dictionary
    for k,v in classmates.items(): print(k,v)
    # loops through the dictionary and gets keys and value, and then prints keys and values
# dictionary looping

def combining_Dictionaries():

    dict1 = {28:'July', 2017:'6'}
    dict2 = {'Emoji':'MOVIE', 'Coming':'July 28'}

    combinedDict = {**dict1, **dict2}
    # combines the two dictionaries, using ** , like how you use it in function parameters

    combinedDict2 = {**dict1, 'dict2':{**dict2}}
# combiningg multiple dictionaries

def useGensNotLists():
    def classic_fibonacci(limit):
        nums = []
        current, nxt = 0, 1

        while current < limit:
            current, nxt = nxt, nxt + current
            nums.append(current)
        return nums
    # this will make a list of the data, which will take up a lot of memory, and it's slower

    # fib via generators
    def generator_fib():
        current, nxt = 0, 1

        while True:
            current, nxt = nxt, nxt + current
            yield current
    # this will store nothing, it'll do one iterable then trash the data and loop again and return the data
    # which is why you need another loop to get the data from the generator
# use generators instead when possible




# ===== Statements =====

def forLoop_With_Else():
    needle = 'd'
    hayStack = ['1','2','b','w','j','i','z','i','q','p']

    for item in hayStack: # loops through every item in hayStack
        if item == needle: # checks if needle is any of the items in hayStack
            print('Found')
            break # if found it prints, and breaks loop
    else: print("not in hay stack") # if not in hayStack then...
    # this runs else if it has not ran break
    # this shows else works with for loops not how to find items in a list.


    needle2 = 'z'
    hayStack2 = [1,2,6,'asd','b','w','o','asd','iji','zge']
    if needle2 in hayStack2: print("it's in there")
    # basically does the same thing, it goes through the list and tries to find needle2 in it
    else: print("It's not in there!")
# for loop with a else statement at end

def try_Except_Input():
    # keeps asking user for a usable input.
    while True:
        try:
            inp = int(input("Number > "))
            break  # breaks loop if input is a integer
        except:
            print("NOPES!!!!!!")  # prints this if exception happens
        finally:
            print("loop1")  # prints this whether it worked or not
        # a reason to use finally instead of just using a print statement like below.
        # is that this well still run even if you call break in try: , but the print statement below won't run because you broke the loop before it could.
        print("UM LOOP?")
        # this well print at each loop, but won't if you break the loop in the try/except
# using try/except to make sure you get usable input. like if you need a integer but user gives a string.

def try_Except_Finally():
        # try/except/else/finally
        x = 1  # a integer
        try:
            print(int(x))  # tries to convert to integer and print
        except Exception as e:
            print(e)  # you can have multiple exceptions, and the as e part well print out the error
        except:
            print("didn't work, don't know what went wrong")  # if it fails to convert, it prints 'didn't work'
        else:
            print(
                "worked")  # if it did work it prints 'worked'. you should only really have the code that has a chance of crashing in try: , and if does work run else:
        finally:
            print("Done")  # runs this no matter what
        # finally well still run if you don't have except and the IDE gives your an error.

        # if you don't have finally and you just have a print statement after the try and it gives you the error, it won't run the print statement.
        # e.g >
        y = 'hi'
        try:
            print(int(y))  # this well fail
        except:
            print("um")
        print("Done")  # this well not run, since you'll get an error which well stop the whole program

        # converting str to int
        # y2 = 'bye'
        y2 = 1
        try:
            print(int(y2))  # this well still fail
        finally:
            print("Done")  # but this well run though, this well run before you see the error

        # exception as e:
        print('\n\n')
        try:
            x = int("HI")  # tries to convert string to int, (obviously won't work)
        except Exception as e:
            print(
                e)  # instead of crashing the whole program this well catch exception and give you a basic summary of what happened

        # raising your own exceptions
        try:
            x = str("HI")  # convert a string to a string, (this well work)
            if x == 'HI': raise Exception
            # checks if x is 'hi', if so it raises the Exception error itself, you do have to have a except: Exception for this to work.
            # this works with other python errors, you can raise any of them, but you do need except <Error>:
            # if you raised a ZeroDivisionError for example; and you don't have that in a except: below, this well crash
        except Exception:
            print("WRONG!!!")
        # if the try: fails this runs, but even if try: works and the if/else is true then it'll raise this exception
        # try: except: else: finally:

def param_Args():
    
    def getName(first, last):
    # when you call this function you HAVE TO input some type of argument (unless you use default args).
        print('Hello {} {}'.format(first, last))  # for more on the {} and .format() go up to the strings function

    getName('July', '28')

    def getList(*Items):
    # if you don't know how much input you're going to get use *args to catch all of then. 
        print('You have', len(Items), 'items on your list')
        print(Items)

    getList('Emoji', 'FGSP', 'JULY 28', 'Banana', 'lolz')
    # when all of arguments you input will be a list as Items


    def getName2(first='John', last='Doe'):
    # if the function takes input but doesn't NEED to, you can have it have default parameters if function doesn't get any
        print('Hey', first, last)
    # go to dictionaries in baiscs.py
    getName2()

    def getList2(**stuff):
        print('Everything:\n', stuff)
        # prints everything in stuff, stuff is a dictionary, so if you want to call a specific list use the key
        try: print("stuff[grocery]:", stuff['grocery'])  # to call the key from a dict, it HAS to be in quotes. unless changed other wise
        except: print("grocery list doesn't exist")
        # Almost always use try/except when doing something like this, since the function might not get what it needs to. because you can't set default **kwargs params. or the program will crash.
        try: print("stuff[toys]:", stuff['toys'])
        except: print("toys list doesn't exist") 

    getList2(toys='Fidget Spinner, Emojis')



# Parameters and Arguments.

