import builtins
from collections import Counter
from collections import namedtuple
import heapq as hq
from struct import *
import threading as t
# muilti threading
import operator as op
from bs4 import BeautifulSoup as BS
# Internet interaction
import string as st
from PIL import Image
# image editing
from PIL import ImageFilter as IF
# Pillow image edit
import random as rd
# math random generator
from operator import attrgetter as atrg
import functools as funcT
import os
# os interaction tools
import datetime as dt


# ===== Python built in methods =====

def repr_str():
    # repr - unambiguous, str - readable
    x = [1, 2, 3, 4, 5, 'hi', "bye", '1', "2", [1], ("2")]
    y = "Hello World"

    print(str(x))
    print(repr(x))

    print(str(y))
    print(repr(y))

    x = dt.datetime.today()
    y = str(x)
    print()
    print(str(x))  # prints out string version of x
    print(str(y))
    print()
    print(repr(x))  # prints out repr version of x
    print(repr(y))

    # so think of repr is for debugging and developers, and str for users using the program. this is usually used in classes
    # this is usually used as a class attr(a dunder), def __str__(self): or def __reptr__(self):


# repr() vs str()

def Eval():
    for dirItems in dir():
        if not dirItems.startswith('_'):
            print('Deleted:', dirItems)
            del globals()[dirItems]

    def func1():
        print("You called func1")

    def func2():
        print("You called func2")

    def func3():
        print("You called func3")

    # creates functions to call

    eval(input("Call func1,func2 or func3 with (), or try other functions\n> "))
    # be-careful what you let users access, in this case the user can basically do anything -
    # they can call other function outside of this one e.g. key_Sort(), and they can do other commands. like delete create new data etc

    # you should use this after you limited what user can input, like int str or limit the scope that they can call things.
    eval(input("Input try to call outside objects > "))
    # TEMP , for right now the only way is to delete the other object(vars, funcs, etc) that you don't need.
    # a better way to if you don't need to call a function or something else is to convert with int or str etc


# eval

def errors_Exceptions():
    # errors and exceptions
    pass


# errors and exceptions handling

def scopes_LEGB():
    # Local, Enclosing, Global, Built-in
    # all of this think about it as if it's not in this function, the function is to make the file more neat. think of it if everyting inside the scopes_LEGB() function was not in  the function.
    # the global in the function well not work properly when in this scope_LEGB() function.

    x = 'Global x'
    y = 'Global y'

    ### Global variables ###

    def test_Func():
        global y  # this well now use the outside y variable, and any changes from inside function well reflect outside
        y = 'Local y'  # since we have global y changes from 'Global y' to 'Local y' everywhere, even outside of function
        ### Local Variable ###
        print(y)
        # LEGB is the order python checks to find object, if it doesn't find it in the local function, then enclosing then finds one in global it stops and calls that

    def test_Func2():
        global xy  # you don't even need a existing variabale to use global
        xy = 'Local xy'  # since we have global and we made xy = 'Local xy' you can call this from inside function AND outside

    test_Func2()  # you do have to call the function before calling a variable that was made inside the function, if a variable was made outside of function but edited within function, you'll just get the original data
    print(xy)
    # this well work and it'll print the xy from the function, but the function does has to be called first or the variables has be in memore somehow

    test_Func()
    print(y)  # this well print the new variable data from function

    # print(y) # this well not work, since it only exists in the local scope of the function, unless you use global or  return then y = test_Func()

    ### Built-in ###

    minNum = min([1, 2, 3, 5, 6, 2, 9, 1])
    # min() is a built in function in python
    print(minNum)  # prints out smallest number from list

    print(dir(builtins))

    # this well print out all python function and exception errors and more, ex. print, pow, min, ZeroDivisionError, list, etc

    def min():
        pass

    # you have to be-careful when you overwrite a python functino like this. there already is a python functino called min, but you overwrote it with your own function. Python doesn't prevent this so BE CAREFUL
    # print(min([1,2,3,5]))
    # this well show error, since it's calling your min function instead of python default one.

    ### Enclosing ###
    x = 'Global x'

    def outer_Func():
        x = 'Outer x'  # create a local variable in this function

        def inner_Func():
            nonlocal x  # this well edit the outer_Func() x variable also, global well not work in this case
            x = 'Inner x'
            print(x)  # this well print 'Inner x'

        inner_Func()  # calles local function
        print(x)  # prints 'Inner x' even though it looks like it'll print out 'Outer x' since there in the same scope

    outer_Func()
    print(x)  # this well print 'Global x'


# # uses builtins. scopes_LEGB()

def Pythonic_EAFP_vs_LBYL():
    # pythonic way of doing things. EAFP: Easier to Ask Forgiveness then Permission
    # basically saying don't have program keep asking if it can do something, just do and and if it fails handle it
    # LBYL: Look Before You Leap. this can work in some cases where you need to be extra careful and/or you can't have any error or miss-haps, but in most cases it'll probably won't hurt using EAFP

    class Test:
        def Func1(self):
            print("I'm Function 1")

        def Func2(self):
            print("Hey Function 2 here")

        def Func3(self):
            print("HI FUNCTION 3 RIGHT HERE!!")

    # LBYL. This well see if the class method exists then see if it's callable, then call it. (Non-Pythonic)
    if hasattr(Test, 'Func1'):  # checks if the Test class has a attribute in this case a Func1 method
        if callable(Test.Func1):
            Test().Func1()
        # Test does have Func1, then it checks if it's callable, if so again it'll then call it
    if hasattr(Test, 'Func2'):
        if callable(Test.Func2):
            Test().Func2()
    if hasattr(Test, 'Func3'):
        if callable(Test.Func1):
            Test().Func3()

    # this way of coding is a somewhat exagrated way of putting it, but if you have to ask and then check the function to see if it exist or callable, it might get tediouse after a while

    print()
    # EAFP. this well try to run all the class methods, and if any of them fail then it'll handle it. (Pythonic)
    try:
        Test().Func1()
        Test().Func2()
        Test().Func3()
        # this well try to call all of the class methods, usually you'll want them seperate or maybe not, since this well actually tell you which one failed.
    except AttributeError as e:
        print(e)
    # if any of them fail, then it'll show the exception


# when to be-careful and not be and handle errors

def bit_Wise():
    # Binary AND #
    a = 50  # 110010  -  32 + 16 + 2 = 50
    b = 25  # 011001  -  16 + 8 + 1 = 25
    # if 1 + 1 = 1, 0 + 0 = 0, 1 + 0 = 0, 0 + 1 = 0
    c = a & b  # 010000  -  0 + 16 + 0 + 0 + 0 + 0 = 16
    # 32 16 8 4 2 1  -  binary. (binary clock)

    # Binary RIGHT
    x = 240  # 11110000  -  128 + 64 + 32 + 16 = 240
    y = x >> 2  # 00111100  -  32 + 16 + 8 + 4 = 60
    z = x << 4  # 00001111  -  8 + 4 + 2 + 1 = 15

    # 128 64 32 16 8 4 2 1  -  this can continue for ever.


# byte data ,learn some binary


# ===== lists/tuples/dicts =====
def unpacking_Args():
    def health_calc(age, apples_ate, cigs_smoked):
        answer = (100 - age) + (apples_ate * 3.5) - (cigs_smoked * 2)
        print(answer)

    data = [27, 20, 0]  # creates data to input to function
    health_calc(*data)  # unpacks data and uses each item as a parameter. **kwargs is for mapping


# unpacking arguments

def mapping():
    data = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]  # some data
    print("Original Data:", data)  # prints original(untouched data)

    def multiply_Add(x): return x * x + x

    # basic function multiples number by itself and adds itself. 1 * 1 + 1 = 2

    newData = []  # new blank list
    for i in data:  # loops through every item in the list
        newNum = multiply_Add(i)  # runs the function and puts the new number(of this current loop) into a new variable
        newData.append(newNum)  # appends the new variable into the newData list
    # you can compress this down to > for i in data: newData.append(multiply_Add(i)), but this was to show how much faster and easier map in this case
    print("Data from for loop:", newData)  # prints new list

    newData2 = list(map(multiply_Add, data))
    # makes a new list newData2 from running the multiply_Add function on each item in data list.
    print("Data from map:", newData2)  # prints the second new list


# use map() on a list

def unpack_Lists_Or_Tuple():
    date, name, price = ['december 12', 'thingy',
                         5]  # the variables correspond to the items in the correspsonind position
    firstItem, *aLotOfThings, lastThing = ['this is first item', 'middle item 1', '2', '3', '4', 'last middle item',
                                           'last Item in list']
    # firstItem well equal the first item in the list, and lastThing well be the last item in list
    # everything in between well be a list of it's own in aLotOfThings
    print(aLotOfThings)

    def unpack_Fist_Last(grades):
        first, *middle, last = grades
        avg = sum(middle) / len(middle)
        return avg

    print(unpack_Fist_Last([54, 83, 99, 23, 64, 85]))


# more on using lists/tuples

def namedTuple():
    color = (55, 155, 255)  # a normal tuple that represents RGB

    ntColor = namedtuple('Color', ['red', 'green', 'blue'])
    # sets color names

    colors = ntColor(55, 155, 255)
    print(colors.red)  # grabs red value


# uses namedtuple from collections as ntup

def key_Sort():
    def lines():
        print('-' * 50)  # prints line seperator

    stuff = [{"Name": 'Kirby', 'Color': 'Pink'},
             {"Name": 'Keeby', 'Color': 'Yellow'},
             {"Name": 'MetaKnight', 'Color': 'Blue'},
             {"Name": 'WaddleDee', 'Color': 'Orange'},
             {"Name": 'Dedede', 'Color': 'Yellow'},
             {"Name": 'Emoji', 'Color': 'Yellow'},
             {"Name": 'Rhino Virus', 'Color': 'Blue'},
             {"Name": 'Brain Cell', 'Color': 'Grey'},
             {"Name": 'Brain Cell', 'Color': 'Gray'},
             {"Name": 'Smiley', 'Color': 'Red'},
             {"Name": 'Smiely', 'Color': 'Red-ish'}]

    print("Name: {} | Length: {} | Sort: {}".format('stuff', len(stuff), 'Name:Color'))
    # prints out info about list
    print("-Original List-")
    for i in stuff: print(i)  # prints each dictionary from list
    lines()
    print("\n-Sorted By Name-")
    lines()
    for x in sorted(stuff, key =op.itemgetter('Name')): print(x)
    # sorts data by 'Name' key, it doesn't sort by anything else. So if you are using this with names and a lot of people have same name but different last name, it'll not sort by last name alongside first name.

    # in this example look at the sort order of Brain Cell: Grey/Gray and Smily: Red/Red-ish
    # Gray should be before Grey. and Red-ish before Red

    print("\n-Sorted By Name Then Color-")
    lines()
    for x in sorted(stuff, key = op.itemgetter('Name', 'Color')): print(x)
    # this well sort by Name then once sorted it sorts by Color, so if there's duplicate Name's but different Color's it'll sort that


# heapq as hq

def Comprehension():
    # List comprehension is usually used to loop through and to a quick operaiton instead of using a full for loop, even though you can

    genComp = (i for i in range(10))
    # this is a generator, you need another loop to access all the data. like using yield

    listComp = [i for i in range(10)]
    # List comprehension loop

    setComp = {i for i in range(10)}
    # Same as list but a set, not editable and no duplicates

    dictLoop = {k: v for k, v in zip(range(10, 1), reversed(range(10, 1)))}
    # dictionary loop, key:value for k,v in zip(k, value)

    numList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]  # a list of numbers to play with

    # ----- SQR -----
    # loop through and find the square of each nunber then add to a new list
    # for loop
    sqrList = []  # have to create a blank list to put new data in
    for num in numList:  # loops through each item in numList
        sqrList.append(num * num)
        # multiplies num by num to get the sqr of that current number then adds to newList

    # The list way
    sqrList1 = [num2 * num2 for num2 in numList]
    # does the same thing as the for loop from above, just in a more compact way

    # ------ Map with lambda -----
    # this is just an alternative way of doing it
    sqrList2 = map(lambda num3: num3 * num3, numList)

    # does the same thing but

    # List comprehension vs Map
    def do_Something(num):
        return num * num + num / num ** num - num

    # a function

    listFunc = [do_Something(i) for i in numList]

    mapFunc = map(do_Something, numList)
    # you'll have to use a for loop to loop over the data or use list with map e.g. list(map())

    # ----- if Even -----
    ifEvenList = [num for num in numList if num % 2 == 0]
    # this well only add num if num divided by 2 has no remainder, in other words even.

    # in this case you'll probably want to use filter() instead of map() unless you want a list of True/Falses(I mean you might just unlikely)
    filterEvenList = list(filter(lambda n: n % 2 == 0, numList))
    # filter() does the same as map, goes through each item from list and run a function on them,
    # but filter well only return items if the function returns true. and also in the case it'll be a list,
    print("if/else filter() :: ", filterEvenList)

    mapEvenList = list(map(lambda num: num % 2 == 0, numList))
    # this well just return True or False from the lambda, instead of returning the item that went through the function
    print("if/else map() :: ", mapEvenList)

    # ----- Nested -----
    # pair each one letter to every number the the next letter with all the numbers
    letters = 'abcd'
    numbers = range(4)

    # for loop(s)
    pairedList = []
    for letter in letters:  # loop through the letters
        for num in numbers:  # loop through the numbers
            pairedList.append((letter, num))  # append letter with num
    print("For loop :: ", pairedList)
    # >> [('a', 0), ('a', 1), ('a', 2), ('a', 3), ('b', 0) .... ('d', 1), ('d', 2), ('d', 3)]
    # it pairs

    # List Comp(comprehension)
    pairedList2 = [(letter, num) for letter in letters for num in numbers]
    # does the same thing as above but in one line, might be harder to read tho
    print("List Comp ::", pairedList2)

    # ----- Dictionary Comprehension -----
    # long way
    x = {}
    for i in range(0, 99):  # loops through 98 times
        x[i] = rd.randint(0, 99)  # creates a key from i and value as a random int
    print(x)

    # shorter way
    x = {i: rd.randint(0, 99) for i in range(0, 99)}  # same as above just in dict comp form
    # it's very similar to list comprehension but you have to include a key

    names = ['Kirby', 'keeby', 'emoji', 'rhino', 'bob']
    colors = ['pink', 'yellow', 'yellow', 'blue', 'um']
    # creates two lists

    # for loop way for dict
    dictLoop = {}  # blank dict
    for name, color in zip(names, colors):
        # zips them together then name and color get there corresponding values
        if name != 'bob':
            dictLoop[name] = color

    print("Dict from for loop :: ", dictLoop)

    # dictionary comp way
    dictComp = {name: color for name, color in zip(names, colors) if name != 'bob'}
    print("Dict from dict comp :: ", dictLoop)

    # ----- Set comprehension ---
    # very similar to list comp but with sets
    # in this example it shows you basic set comp, even though you could just use set()
    dupeNumbers = [1, 2, 3, 5, 3, 1, 3, 4, 2, 1, 3, 2, 1, 1, 4, 2]
    # a list with duplicate numbers

    # for loop way
    loopSet = set()  # you can't use {} since that's mainly for dictionaries
    for n in dupeNumbers: loopSet.add(n)
    print("For loop set :: ", loopSet)

    compSet = {n for n in
               dupeNumbers}  # this is not a dictionary since you don't have the colon(:) which is for key:value
    print("Comp set :: ", compSet)

    # ----- Generators -----
    numebrs = [1, 2, 3, 4, 5, 6]

    # a regular gen
    def gen_Func(nums):
        for n in nums: yield n * n

    # a generator function

    genNumbers = gen_Func(numbers)
    for i in genNumbers: print(i)

    genExpression = (n * n for n in numbers)
    # you very similar to list comp, but you use parentethese () to say it's a generator, does the same as the function above, it uses yield and you have to use a loop to iter over the items
    for j in genExpression: print(j)


# random as rd module. shows list, dictionary, tuple, generator, etc comprehension. and comparing to map()/filter() and for loops

# ----- Dictionary -----
def heapq_and_ListDicts():
    grades = [15, 74, 93, 55, 67, 91, 23, 49, 89, 23, 87, 67, 38]  # list of data
    print(hq.nlargest(3, grades))  # prints out the three largest items in list

    stuff = [{"Name": 'Kirby', 'Color': 'Pink'},
             {"Name": 'Keeby', 'Color': 'Yellow'},
             {"Name": 'MetaKnight', 'Color': 'Blue'},
             {"Name": 'WaddleDee', 'Color': 'Orange'}]
    # a list of dictionaries
    print(stuff[1]['Name'])
    print(stuff[1]['Color'])

    print()
    for i in range(len(stuff)):
        item = list(stuff[i].items())
        print(item[0][1], ':', item[1][1])

    print()
    print(hq.nsmallest(2, stuff, key=lambda stuff: stuff['Name']))


# heapq usage

def sorting_Dictionary():
    stocksPrices = {'GOOG': 520.20,
                    'FB': 76.87,
                    'YHOO': 39.89,
                    'AMZN': 306.98,
                    'APPL': 100.24}

    unzipped = zip(stocksPrices.values(), stocksPrices.keys())
    sort = sorted(unzipped)  # sorts dictionary low to high by dictionary values
    print(sort)
    Max = max(unzipped)
    Min = min(unzipped)

    # if you wanted to sort by the keys, just reverse the zip params...
    unzipped2 = zip(stocksPrices.keys(), stocksPrices.values())
    # now when calling sorted/max/min it'll sort by the keys


# sorting a dictionary by key or value by numbers or alphabeticalal


# ===== Other Stuff =====
def custom_Objects():
    class User:
        def __init__(self, name, ID):
            self.name = name
            self.userID = ID

        def __repr__(self):
            return self.name + " : " + str(self.userID)

    users = [User('Kirby', 550),
             User('Emoji', 99),
             User('Rhino V', 55),
             User('Smiley', 10),
             User('Brain C', 21)]
    # makes new instances of User

    for user in users: print(user)  # prints out user info from __repr__

    print('-' * 10)

    print("-Sorted by Name-")
    for user in sorted(users, key=op.attrgetter('name')): print(user)
    # sorts by users name. similar to op.itemgetter() for dictionary

    # you have to use the self variable in attergetter to sort by that. e.g. self.uName = name  would be op.attrgetter('uName')

    print('-' * 10)
    print("-Sorted by userID")
    for user in sorted(users, key=op.attrgetter('userID')): print(user)
    # sorts by users ID


# also uses itemgetter

def search_Page_Crawler():
    # basic search page web crawler
    # import requests
    # from bs4 import BeautifulSoup

    searchPageURL = ''  # gets the url for the search pages e.g. site/search/page=1
    mainURL = ''  # gets main page url. e.g. site.com

    def search_Crawler(maxPages, mainURL):  # max pages

        page = 1  # current page
        while page <= maxPages:  # loops until mxa page
            url = searchPageURL + str(page)  # url
            sourceCode = requests.get(url)  # gets source code
            plainText = sourceCode.text  # gets plain text
            soup = BeautifulSoup(plainText)
            for link in soup.findAll('a', {'class', 'item-name'}):  # goes through and only gets class=item-name items
                href = mainURL + link.get('href')  # gets href from data
                title = link.string  # gets title name
                print(title)
                get_Item(href, mainURL)  # calls the function to get even more links from within item
            maxPages += 1  # increments to next page

    def get_Item(itemURL, mainURL):
        sourceCode = requests.get(itemURL)
        plainText = sourceCode.text
        soup = BeautifulSoup(plainText)
        for item in soup.findAll('div', {'class', 'i-name'}):
            print(item.string)
        for link in soup.findAll('a'):  # gets all links from item page
            href = mainURL + link.get('href')
            print(href)

    search_Crawler(1, mainURL)


# crawls search pages and search items

def threading():
    class smallMessenger(t.Thread):
        def run(self):
            for _ in range(50):
                print(t.currentThread().getName())

    x = smallMessenger(name="Send Messages")
    y = smallMessenger(name="Receive Messages")
    x.start()
    y.start()


# threading as t. threading processes

def word_Web_Counter():
    def start(url):
        wordList = []  # word list
        URL = ''  # url to set
        sourceCode = rqs.get(URL).text  # gets text from url
        soup = BS(sourceCode)  # soupy code

        for text in soup.findAll('a', {'class', 'index_singleListingTitles'}):
            # gets html strings
            content = text.string
            words = content.lower().split()  # puts lowercase and splitted words into words
            print(words)
            for eachWord in words:  # appends words to list
                print(eachWord)
                wordList.append(eachWord)

    def clean_Up(wordList):
        cleanedWords = []  # new list of only alphabetic words
        for word in wordList:
            symbols = st.punctuation  # variable of all symbols/puncuation
            for i in range(len(symbols)):
                word = word.replace(symbols[i], "")  # checks whether word has symbol, removes it
            if len(word) > 0: cleanedWords.append(word)  # only appends words no blanks.

        createDictionary(cleanedWords)

    def create_Dictionary(finalWords):
        wordCount = {}  # a new dictionary
        for word in finalWords:
            if word in wordCount:  # checks whether word already exists in dict
                wordCount[i] += 1  # if so adds 1 to the value
            else:
                wordCount[i] += 1  # if not it creates a new key and +1 value

        for k, v in sorted(wordCount.items(), key=op.itemgetter(1)):
            # goes through dictionary and sorts by value by most
            print(k, v)


# bs4.BeautifulSoup as BS | operator as op | requests as rqs | string as st
# counts how words from website, with threading


def image_Edit():
    ### Open Image ###
    img = Image.open('Kirby.png')  # opens image(doesn't show the image though)

    ### Image Info ###
    print(img.size)  # prints image size
    print(img.format)  # prints image format. PNG/JPEG/etc
    print(img.mode)  # prints the image mode. RGB/CMYK/etc

    ### Image Channels ###
    r, g, b, a = img.split()  # splits image to red, green, blue, alpha
    r.show()  # only shows red channel

    ### Channel Merge ###
    mergedImg = Image.merge('RGBA', (r, g, b, a))  # remerges image with all the channels

    blueKirby = Image.merge("RGBA", (g, b, r, a))  # re-arranges channels when merged
    blueKirby.show()  # shows the image, and it'll be blue

    ### Image Edit ###
    flippedImg = img.transpose(Image.FLIP_LEFT_RIGHT)  # flips image left to right
    flippedImg.show()

    spinImage = img.transpose(Image.ROTATE_90)
    spinImage.show()

    ### Change Mode ###
    convertedImg = img.convert("L")  # converts image mode to L (Luminates (Black and White))
    convertedImg.show()

    blurredImg = img.filter(IF.BLUR)  # blurs image. not as good as Photoshop though, or any other actual image editors
    blurredImg.show()

    img.show()  # shows image in default image viewer


# PIL Images, ImageFilter as IF, basic edits on photos, flip,blue,etc

def word_Counter():
    phrase = """Hello World I'm a new program from a computer, I do stuff and more stuff. I like Cheese, yes why can't a computer program like cheese? Do you have something against computers liking cheese???? Why can't computers like cheese? Cheese is yummy......... YOU ARE YUMMY!!!!!!"""

    print(phrase)

    wordsFromPhrase = phrase.split()

    print("\nChar Length:", len(wordsFromPhrase))

    counter = Counter(wordsFromPhrase)
    print("All Words:", counter)
    print("3 Most Common:", counter.most_common(3))


# collections.Counter

def structs():
    packedData = pack('iif', 6, 19, 4.73)  # converts to byte data
    print(packedData)  # print data

    print(calcsize('i'), calcsize('f'),
          calcsize('iif'))  # shows how much memory space it takes to store integer or float or both etc

    unpackData = unpack('iif', packedData)  # converts back to human readable data
    print(unpackData)
    print(unpack('iif', b'\x06\x00\x00\x00\x13\x00\x00\x00)\\\x97@'))  # prints byte data in human readable text/ints


#  sctruct *


# ===== Function =====
def Closures():
    # First-Class Functions and stuff
    def cubed(x): return x * x * x  # returns cubed data

    def sqr(x): return x * x  # simple function that squares the number

    f = sqr
    print(sqr(5))
    print(f)
    print(f(5))

    def my_Map(func, data):
        # accepts a function(without ()) and data in a list
        results = [func(i) for i in data]
        # adds each item from the data param and runs each one through the specified function
        return results

    sqredData = my_Map(sqr, [1, 2, 3, 4, 5])
    # calles my_Map function and sets sqr as function and then inputs this list of data
    print(sqredData)

    cubedData = my_Map(cubed, [1, 2, 3, 4, 5])
    print(cubedData)

    def logger(msg):
        def log_Msg():
            print('log:', msg)

        return log_Msg

    logHi = logger("hi")
    logHi()

    def html_Tag(tag):
        def wrap_Msg(msg):
            print('<{0}>{1}<{0}>'.format(tag, msg))

        return wrap_Msg

    printHi = html_Tag('h1')
    printHi('hello there')
    printHi('hi again!')

    printP = html_Tag('p')
    printP('paragraph!!')

    # ----- Closures -----
    # a inner function that remembers and has access to variables in the local scope in witch it has created, even after when the outer func has finished
    def outer():
        msg = 'hi'

        def inner():
            print(msg)  # prints out msg var from outer()

        return inner()  # since inner has () this well run the function

    outer()

    def outer2():
        msg2 = 'hi2'

        def inner2(): print(msg2)

        return inner2  # this well not run the function

    myFunc = outer2()
    myFunc()

    def outer3(msg):
        msg3 = msg

        def inner3(): print(msg3)

        return inner3

    myFuncs = outer3('hi there')
    myFuncs2 = outer3('how you doing?')
    myFuncs()
    myFuncs2()

    def outer_Func(msg):
        message = msg

        def print_msg(): print(msg)

        return print_msg

    func1 = outer_Func('hi')
    func2 = outer_Func('bye')
    func1()
    func2()


def lambda_Funcs():
    answer = lambda x: x * 2  # small function that takes one parameter. kinda like...

    def answer2(x): x * 2

    # you would usually(99% of the time) the lambda when you want a quick function that you'll use only once, and it's quick and easy
    # if you want somthing that you'll use a lot and that does much more things you would use def

    # an example of where you would use a button in tkinter. this code well not work unless import tkinter
    Button(root, text='This is a button', command=lambda: print("You pressed the button."))
    #  1.    2.      3.                       4.          5.
    # 1) new Button.  2) root frame.  3) text on button.
    # 4) the command for when button is clicked.
    # 5) a simple function that prints out text to console when button is pushed, this can also be a function call, but without ()


# lambda functions

def Decorators():
    # shouldn't run in Decorators()

    # ----- Decorator Functions -----
    def dec_Func(function):
        def wrapper():
            print('From function | Running:', function.__name__)
            return function()  # returns data inputted

        return wrapper  # then returns the returned data from wrapper()

    def aFunction(): print("This is a function!!!")

    aFunction = dec_Func(aFunction)
    # wraps aFunction with dec_Func()
    aFunction()

    # adding this makes it easier, so you don't have to do the aFunction = dec_Function(aFunction)
    @dec_Func
    def aFunction2(): print("Hey look another function. BORING!!!")

    aFunction2()

    def dec_Func2(function):
        def wrapper(*args, **kwargs):  # need to be able to accept any args or kwargs to pass into the function
            print('From Function(*, **) | Running:', function.__name__)
            return function(*args, **kwargs)  # pass args and kwargs into function

        return wrapper

    @dec_Func2
    def arg_Function(name, age): print("You're name is {} at age {}".format(name, age))

    arg_Function('Kirby', 10)

    # ----- Decorator Class -----
    class DecCLass(object):
        def __init__(self, function):
            self.function = function

        def __call__(self, *args, **kwargs):
            print('From __call__ | Running:', self.function.__name__)
            return self.function(*args, **kwargs)  # pass args and kwargs into function

    @DecCLass
    def call_Function(name, color): print("{} is {}".format(name, color))

    call_Function('Kirby', 'Pink')

    # ----- Examples -----
    # Timer
    def timer(function):
        from time import time
        def wrapper(*args, **kwargs):
            start = time()
            func = function(*args, **kwargs)
            stop = time() - start
            print("Time to run '{}': {}".format(function.__name__, stop))
            return func

        return wrapper

    @timer
    def num_Loop():
        for i in range(999999): print(i)

    # num_Loop()

    # Multiple Decorators
    def dec1(function):
        def wrapper(*args, **kwargs):
            print("dec1 | Passed in function:", function.__name__)

        return wrapper

    def dec2(function):
        def wrapper(*args, **kwargs):
            print("dec2 | Passed in function:", function.__name__)

        return wrapper

    # you can have multiple decorators, as seen here. But this well not fully work correctly
    @dec1
    @dec2  # same as func1 = dec1(dec2(func1)
    def func1(extraText): print("Hello World!!!")

    func1()  # this well print out > dec1 | Passed in function: wrapper

    # since really dec1 was passed into dec2 instead of func1, which is what we (usually) want

    # to fix this use @wraps() from the functools modules, (part of Python standard library(so it'll be available when installed python)

    def dec1_2(function):
        @funcT.wraps(function)
        def wrapper(*args, **kwargs): print("dec1_2 | Passed in function:", function.__name__)

        return wrapper

    def dec2_2(function):
        @funcT.wraps(function)
        def wrapper(*args, **kwargs): print("Uh")

        return wrapper

    @dec1_2
    @dec2_2
    def func2(extrText): print("Hello World AGAIN!!!")

    func2("BOOO")


# Decorators  @dec

def decorator_Args():
    # do not run in this function, un-indent everything first

    def prefix_Func(prefix):
        def dec_Func(originalFunc):
            def wrapper_Func(*args, **kwargs):
                print(prefix, "Running before:", originalFunc.__name__)
                result = originalFunc(*args, **kwargs)
                print(prefix, "Ran after:", originalFunc.__name__)
                return result

            return wrapper_Func

        return dec_Func

    @prefix_Func("LOL")  # calls decorator function and passes in argument
    def afunc1(text, int):
        print(text * int)  # a new function that takes in 2 arguments

    afunc1("Hellow World", 16)  # calling function

    # better example of decorators
    def passThrough(func):  # this is the decorator function
        def wrapper(*args, **kwargs):
            try:
                print("::INPUT::\n%s\n%s" % (args, kwargs))  # prints args and kwargs passed in
                kwargs['nums'] = str(kwargs['nums'])
                # tries to convert kwarg 'nums' to a string
            except:
                print("ERROR: %s.passThrough.wrapper" % func.__name__)
                # prints an error. func.__name__ gets the function name instead of memory location
            finally:
                print("::OUTPUT::\n%s\n%s" % (args, kwargs))
                return func(*args, **kwargs)  # passes in the args and kwargs back into the function
                # this will run if it worked or not

        return wrapper

    @passThrough
    def anotherFunc(*args, **kwargs):
        print("::anotherFunc::")
        print("nums type:", type(kwargs['nums']))  # prints what data type 'nums' is
        print("%s\n%s" % (args, kwargs))

    # if this works right, 'nums' should always be a string, even if you input other data, like numbers
    anotherFunc(nums=1)


# decorator function that can take arguments


# ===== Class =====


def Classes():
    var1 = 'from outside of class'
    var2 = 'um'

    class Kirby:  # a class
        classVar = 12
        classvar2 = 'insisde class'

        # class variables, can be called anywhere in the class

        def __init__(self, aNum):
            # an init function, this well run every-time a class instance is made
            # you do need to make a new instance of the class if ou want to call or access anything from within it, unless you have a @classmethod
            print("Started Class")
            self.selfInitVar = aNum + aNum
            # this variable can be accessed in anyother part of the class(even within function(called a class method)
            initVar = aNum * aNum
            # this can only be accessed in this function(class method), you cannot call it from another part of the class
            # init variable, these well always be set when a new instance of the class is made

        def aFunc(self):
            funcVar = 'a regular variable lalalala'  # like from above this var can only be accessed in this function
            self.selfVar = 'hiya a;sdfsaf'
            # this var can be accessed in other parts of the class, but the function(technically a method in a class) has to be called first to declare it first
            print("From a regular Function")

        @staticmethod
        def static_Method():
            staticVar = 'STATIC!!!'
            print("From Static Method")

        def another_Func(self):
            print(var1)  # printint class variable

        @classmethod
        def class_Method(cls):  # cls is only used for class methods
            classVar = 'CLASSY!!!'
            print("From a class METHOD")
            print(classVar)

    Kirby.class_Method()
    # runs only the class_Method() from the Kirby class, it doesn't need an instance to call it, unlike the other ones, a staticmethod doesn't need an instance either
    # so this well only do what the class_Method() has, so you won't get the "Started Class' print, you can also do Kirby().class_Method() to start an instance, this well work too
    # you call the static method the same way, Kirby.static_Method() or Kirby().static_Method()


# basics of a class, also @classmethod and @staticmethod


def Dunders():
    # Regular way and the Dunder way
    # Adding
    print(1 + 1)
    print(int.__add__(1, 1))

    # Subtracting
    print(1 - 2)
    print(int.__sub__(1, 2))

    # Multiplying
    print(2 * 2)
    print(int.__mul__(2, 2))

    # dividing
    print(10 / 5)
    print()

    # Strings
    print('a' + 'b')
    print(str.__add__('a', 'b'))

    # uses operator.itemgetter module - op


# Special Methods. __add__ / __sub__ / __len__

def inherit_Class():
    # class parent and child
    class ParentClass:  # create parent class
        age = 12
        name = 'Kirby'  # class variables
        cuteness = 100

    class ChildClass(ParentClass):  # new class but has all of data/variables/funcs from parent
        mood = 'Happy'
        color = 'Pink'
        location = 'Bed'

    class AnotherClass(ChildClass, ParentClass):  # inherits multiple classes
        number = 123456789
        email = 'Kirby550@KMail.com'
        address = '550 DreamLand'

        age = 13  # you can override things from parent class, funcs/variable/etc

    Kirby1 = AnotherClass()  # new class instance with all of the inheritances
    print(
        Kirby1.age)  # even though you made a AnotherClass instance, since it's a child class you can call the parent(s) data.


# class inheritance, child and parent classes

def checking_ifClass_orSubclass():
    class Kirby:
        def bePink(self): print("I'm Pink!")

        def likeCake(self): print("I love cake!!!")

    class Person:
        def beStupid(self): print("I'm not stupid")

        def beBreathing(self): print("Am i breathing??")

    def check(x):
        if isinstance(x, Person):
            print("He's a person")
        # this checks if the instance passed in as x is from class Person, if sooo.. then prints this
        elif isinstance(x, Kirby):
            print("It's a cute Kirby")
        # this checks if it's a instance of class Kirby
        else:
            print("Dunno what it is")
        # if it's neither

    person1 = Person()  # new Person instance
    check(person1)  # runs funciton
    kirby1 = Kirby()  # new Kirby instance
    check(kirby1)

    class upper:
        def __repr__(self): (self): print("Upper class")

    class sub(upper):
        def __repr__(self): (self): print("Lower class")

    def ifSub(x):
        if isinstance(x, upper):
            print("It's a subclass of class upper")
        else:
            print("it's not a subclass of upper")

    U = upper()
    ifSub(U)
    S = sub()
    ifSub(S)


# shows using isinstance() and issubclass(), to see if that instance is from a specfiic class or it's a subclass

def basic_Game_Class():
    class Enemy:
        def __init__(self):
            self.life = 3

        def attack(self):
            print('ouch')
            self.life -= 1

        def check_Life(self):
            if self.life <= 0:
                print("DEAD!")
            else:
                print("Life left:", self.life)

    enemy1 = Enemy()


# learn about classes for games

def sort_Class_Obj():
    class Employee:
        def __init__(self, name, age, salary):
            self.name = name
            self.age = age
            self.salary = salary

        def __repr__(self): return ("{}, {}, ${}".format(self.name, self.age, self.salary))

        # when using print on a class instance this is what it'll return.

    e1 = Employee('Kirby', 10, 10_000)
    e2 = Employee('Emoji', 15, 11_000)
    e3 = Employee('Rhino', 13, 9_000)
    # new class objects

    emps = [e1, e2, e3]  # put them in a list

    def e_Sort(emp): return emp.name

    # this function basically tells sort what to sort by, you can change the emp.name to any of the other data; salary, age, etc
    print("Sorted by name :: ,",
          sorted(emps, key=e_Sort))  # print out class object sorted by the key which well return the name.
    # just using sorted(emps) well not work, since it doesn't know what to sort by, IT'S NOT like a dictionary
    # the key is what it'll sort by

    print("Sorted by age :: ", sorted(emps, key=lambda e: e.age))
    # you can use a function if you want something more complex, or just use a lambda; which is much faster and cleaner

    print("Sorted by Salary with attrgetter :: ", sorted(emps, key=atrg('salary')))
    # instead of using lambda or a function, you can user attergetter from the operator module, also very easy and fast
# uses attrgetter as atrg module
