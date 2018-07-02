import math
import string as st
import operator as op
# you should use better methods when making a real program e.g. using the try/except if you need a specific data type from user.
# also with functions usually you would usually use return, instead of printing from the functions.
# but this is a learning and test file. so use better coding methods then this. this file only shows basic principals on how to use Python in different ways.

def Q1():
    for i in range(2000, 3200):
        if (not i % 7) and (i % 5): print(i)
            # checks to see if divisible by 7 and not by 5

def Q2(num):
    return num * Q2(num - 1)

def Q3 (num):
    num_dict = {} # blank dictionary
    for i in range(num):  num_dict[i] = num * i # creates a key 1 - num and value num time i
    print(num_dict)

    # V2
    num_dict2 = {i: num * i for i in range(num)}
    print(num_dict2)

def Q4():
    numbers_tuple = () # empty tuple
    numbers = input("Input Numbers > ")    # gets input
    numbers = numbers.split(',')
    # makes a list with from input seperated by comma
    numbers_tuple = tuple(numbers)
    # makes a tuple from the list
    print(numbers)
    print(numbers_tuple)

    # V2

    numbers2 = int(input("Numbers > ").split(','))
    # makes list from input
    numbers2_tuple = tuple(numbers2)
    # converts numbers2 list to a tuple

class Q5:
    def __init__(self): self.String = ""
        # starts String instance,

    def getString(self): self.String = str(input("something > "))
        # ask for string input
    def printString(self): print(self.String.upper())
        # prints out String in uppercase

    # this was to demonstrate classes and class functions, if you wanted to just do the uppercase part >
    # print(input("String > ").upper())

def Q6():
    D = input("Numbers > ")
    # gets input
    D = D.split(',')
    # makes list by comma separation
    ans = [] # empty list
    for i in D:
        Q = (2 * 50 * int(i))/ 30 # runs formula with every item in D list
        sqrt = Q**(1/2) # gets square root for every item
        # could'v also used >
        Q2 = int(math.sqrt((2 * 50 * int(i))/30)) # runs formula then uses sqrt function from math module, then converts to integer
        ans.append(int(sqrt)) # appends the finish product to ans list
    print(ans)

    # V2
    # you could also >
    D2 = input("Numbers > ").split(',')
    # takes the input ans instantly makes a list from input with comma separated
    ans2 = [int(math.sqrt((2 * 50 * int(j))/30)) for j in D2]
    # runs formula with every item in D2 and converts to integer then adds to ans2 list
    print(ans2)

def Q8():
    Words = sorted(input("Words > ").split(','))
    # sorts the spliced data data alphabetically.
    # so you input data, it splits it by spaces, then sorts.
    print(''.join(Words))
    # rejoins the data and prints data.

def Q9():
    str1 = str(input("Input some text > "))
    return str1.upper()
    # outputs string input all uppercase

def Q10():
    usrInp = input("Input some text > ") # gets user input
    toString = str(usrInp) # converts input to string
    splitString = toString.split() # splits data by space
    sortedString = sorted(splitString) # sorts string input alphabetially
    noDupes = set(sortedString)
    outPut = ' '.join(noDupes)

    # quicker version

    usrInp2 = input("Input some text 2 > ") # gets user input
    return ' '.join( sorted( set( usrInp2.split() ) ) )
    # 1.      2.        3.    4.     5.    6.
    # 1) returns data(not print).  2) rejoins data.  3) sorts data.
    # 4) makes a set, basically removes duplicates.  5) gets data from usrInp2
    # 5) splits data by spaces.  So this well get data from input, then splits it then makes a set from it,
            # sorts data and rejoins it to return

def Q11():
    inp = input("4 Digit Binaries, seperated by ',' > ").split(',')
    print(inp)
    # test data. 0100,0011,1010,1001,0101,1111
    for i in inp:
        if int(i,2) % 5 == 0: print(int(i, 2),':', i)

def Q12():
    values = []
    for i in range(2000, 3001):
        s = str(i)
        if (int(s[0]) % 2 == 0) and (int(s[1]) % 2 == 0) and (int(s[2]) % 2 == 0) and (int(s[3]) % 2 == 0):
            values.append(s)
    print(",".join(values))

    for j in range(2000, 3001):
        if j % 2 == 0: print(j,end=',')

def Q13():

    letterNum, digitNum = 0, 0 # creates variables, to count how many letters and numbers
    usrInp = str(input("Input some stuff > ")) # gets user input

    for i in usrInp: # loops through each letter/int from input
        if i.isdigit(): letterNum += 1 # checks for a letter. a-z - A-Z
        elif i.isalpha(): digitNum +=1 # checks whether current item is a number. 0-9

    print("Letters: {}\nNumbers: {}\n".format(letterNum, digitNum))
    # prints out results. can use two print statements, bbuuuuuut idc.

def Q14():
    inp = list(input("Input some text > "))
    upper = [letter for letter in inp if letter.isupper()]
    lower = [letter for letter in inp if letter.islower()]
    print("Uppercase:", len(upper), upper)
    print("Lowercase:", len(lower), lower)

def Q15():
    x = str(input("A Number please > "))
    ans = int(x) + int(x+x) + int(x+x+x) + int(x+x+x+x)
    print(ans)

def Q16():
    usrInp = input("Input numbers separated by comma > ").split(',')
    # gets user input and seperates by comma
    newList = [int(i) for i in usrInp if int(i) % 2 != 0]
    # only adds odd numbers to list. it converts to integer from string
    print(newList)

def Q17():

    class aBank:
        def __init__(self): self.balance = 0 # creates a new instance balance of 0

        def withdrawal(self, amount): self.balance -= amount # takes money away from balance

        def deposit(self, amount): self.balance += amount # adds money to balance

    startBank = aBank() # a new instance of aBank, so balance well start at 0

    while True:
        usrInp = input("W/D Amount, or done > ") # gets user input

        i = usrInp.split(' ') # splits command by space. so you'll have D/W and then amount

        if i[0] in ('Done','done'): break # loops through until user says done, the it breaks the loop

        if i[0] == 'D': # checks if user wanted to deposit
            print("Depositing:", int(i[1]))
            startBank.deposit(int(i[1])) # if so it calls the deposit method from aBank class
        elif i[0] == 'W': # checks if wanted to withdrawal
            print("Withdrawing:", int(i[1]))
            startBank.withdrawal(int(i[1])) # if so call the withdrawal method from class
        else: print("That's not a command") # prints if not usable command

    print("Final Balance:", startBank.balance) # prints final balance

def Q17_2():
    # Q16() is usually a better way to do something like this, because it uses class you can later add more functionally later. and it'll be easier when you add more functions/methods.
    netAmount = 0 # starts with 0 balance
    while True:
        print("blank to stop, D - deposit, W - withdrawal") # some useful info
        s = input("> ") # gets user input
        if not s: break # if you input nothing it breaks the loop
        values = s.split(" ")
        operation = values[0]
        amount = int(values[1])
        if operation == "D": netAmount += amount
        elif operation == "W": netAmount -= amount
        else: pass
    print("Final Balance:",netAmount)

def Q18():
    paswordInp = input('Password > ').split(',') # gets input from user, then separated by comma

    workedPass = [] # a list of worked password

    # sets punctuation, number, uppercase, lowercase to falls
    for Pass in paswordInp: # loops through each item from passwordInp
        punc = nums = uL = lL = False # sets punctuation, number, uppercase, lowercase to False
        # all of these have to be True to have a working password

        if 6 < len(Pass) < 12:
        # makes sure that the current pass is longer then 6 and shorter then 12, if it isn't it won't go on
            for l in Pass:
            # loops through each letter in password
                if l in st.punctuation and st.digits: # checks if l is in ...
                    punc = nums = True
                if l in st.ascii_uppercase and st.ascii_lowercase:
                    uL = lL = True
            if punc and nums and uL and lL: workedPass.append(Pass)
            # checks if the current password has a punctuation, number, uppercase and lowercase, if soo the password is added the list
    print("Worked Password:", workedPass)
    # Test data: ABd1234@1,a F1#,2w3E*,2We3345, af!3kfDD

def Q19():
    inputData = input("Input Name, Age, Score > ").split('.') # gets input, splits by '.' name, age, score. to input another set of data, you can use a loop to input line by line
    dataSets = []
    for obj in inputData: # loops through each object by '.' Ex. bob, 12, 44. sarah, 15, 53. tom, 53, 88
        dataSets.append(obj.split(','))
    dataSets = sorted(dataSets, key=lambda x: x[0])
    # sorts each tuple set by the first item in tuple, you can change this by change x[0]
    print(dataSets)
    #Test data: df, 12, 53. af, 53, 35. df, 53, 14

def Q19_2():
    dataList = [] # list of list data, name, age, score
    while True: # loops until you enter blank
        inp = input("Input data > ") # get input
        if not inp: break # if you don't input anything, it'll break the loop and run the other code
        dataList.append(inp.split(',')) # adds data list to the list

    sortedDaa = sorted(dataList, key=op.itemgetter(0, 1, 2))
    # sorts dataList with priority of name, age, then score, then puts it in a new list, so if you have the same name item then it'll sort by the age
    print(sortedDaa)

def Q20():
    class Q:
        def generatorFunc(self, n):
            for i in range(n):
                if i % 7 == 0: yield i

    x = Q()
    for i in x.generatorFunc(50): print(i)

    # or ust generator comprehension
    print("Generator comprehension: ")
    n = range(50)
    generator = (i for i in n if i % 7 == 0)
    for i in generator: print(i)

def Q21():
# don't run in Q21 function
    class Robot:
        def __init__(self):
            self.pos = (0, 0)
            self.Get_Command()

        def RIGHT(self, move):
            self.pos = (self.pos[0] + move, self.pos[1])
            # updates position to move right 'move' amount of times
            print("Moved right", move)

        def LEFT(self, move):
            self.pos = (self.pos[0] - move, self.pos[1])
            print("Moved left", move)

        def DOWN(self, move):
            self.pos = (self.pos[0], self.pos[1] - move)
            print("Moved down", move)

        def UP(self, move):
            self.pos = (self.pos[0], self.pos[1] + move)
            print("Moved up", move)

        def Get_Command(self):
            while True:
                self.inp = input("LEFT/RIGHT/UP/DOWN/STOP X > ").lower().split()  # splits this to command and the number
                try:
                    if 'right' in self.inp[0]: self.RIGHT(int(self.inp[1]))
                    # checks if command is right or r then runs RIGHT function and passes in second item from inp
                    elif 'left' in self.inp[0]: self.LEFT(int(self.inp[1]))
                    elif 'up' in self.inp[0]: self.UP(int(self.inp[1]))
                    elif 'down' in self.inp[0]: self.DOWN(int(self.inp[1]))
                    elif 'stop' in self.inp[0]:
                        print('Final Position', self.pos)
                        print('Distance from original', int( round( math.sqrt( (self.pos[0] ** 2) + (self.pos[1] ** 2) ) ) ) )
                        break
                    # if stop then breaks loop then prints position
                    else:
                        print("Error Try Again:")
                        self.Get_Command()
                except: print("Error")

def Q22():
    inp = input("Input some text: ").lower().split()

    wordDict = {}
    for word in inp:
        wordDict[word] = wordDict.get(word, 0)+1

    print(wordDict)

def Q23():
    def square(x): return x ** x
    square(5)

def Q24():
    print(int.__doc__)
    print(sum.__doc__)
    print(input().__doc__)

    def aFunc(x):
        """This function adds and subtracts x"""
        return (x + x) - x

    print()
    print(aFunc.__doc__)
    print(aFunc(3))

def Q25():
    class AClass:
        def __init__(self, string):
            print(string)

    AClass("Hello World")

def Q26():
    pass



