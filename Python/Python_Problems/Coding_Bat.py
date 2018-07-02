class warmup_1:
    def sleep_in(): pass

    def monkey_trouble(a, b):
        if (a and b) or (not a and not b): return(True)
        else: return(False)
        # this checks if a and b are both true or both false
        # to run, print out the function

    def sum_double(x, y):
        if x == y: print((x + y) * 2)
        else: print(x + y)
        #checks if x and y are the same, if so it returns double of there sum
        #if not it just returns there sum
    def diff21(x):
        if x != 21: print(abs(x - 21))
        else: print(0)

    def parrot_trouble(a, x):
        if (a == True) and (x > 7 or x < 20):
            return True
        else: return False
        #checks if the parrot is talking between 7 and 20
    def parrot_trouble2(a, x):
        return (a and (x < 7 or x > 20))

    def makes10(x, y):
        return (x == 10 or y == 10 or x + y == 10)
        # checks to see if x or y is 10, or if the sum is 10

    def near_hundred(x):
        return ((90 <= x <= 100) or (190 <= x <= 200))
        #checks to see if x is near 100 by 10, or near 200 by 10
    def near_hundred2(n):
        return ((abs(100 - n) <= 10) or (abs(200 - n) <= 10))

    def pos_neg(x, y, a):
        if a : return x < 0 and y < 0
        else: return ((x < 0 < y) or x > 0 > y)

    def not_string(str):
        str.lower()
        if str.split()[0] == 'not': print(str)
        else: print('not', str)
        #checks to see if 'not' is the first word of string, if not it adds it. if so does nothing.

    def missing_char(Str, n):
        Str_ls = list(Str)
        del(Str_ls[n])
        print(''.join(Str_ls))
        #removes the letter from giving position

    def front_back(Str):
        if len(Str) <=1 :
            print(Str)
        else:
            Str_ls = list(Str) #makes string into list
            Ll = Str_ls[0]
            Fl = Str_ls[-1] #puts the first and last letter into variables
            del(Str_ls[0], Str_ls[-1]) #removes first and last letter
            Str_ls.append(Ll) #adds first letter to end
            Str_ls.insert(0, Fl) #adds last letter to beginning
            print(Str_ls)
    def front_back2(str):
        if len(str) <= 1:
            return str
        mid = str[1:len(str) - 1]  # can be written as str[1:-1]

        # last + mid + first
        return str[len(str) - 1] + mid + str[0]

    def front3(Str):
        print(Str[0:3]*3)

def string_times(str,n):
    print(str * n)

def print1(Str):
    for i in range(len(Str)):
        if i % 2 == 0: print(Str[i], end='')
#####   #####   #####   #####   #####   #####   #####   #####
# String-1 #

def hello_name(Name):
    print("Hello", Name)

def make_abba(Str1, Str2):
    print(Str1+Str2+Str1+Str2)

def make_tag(Tag, Txt):
    BeginTag = "<"+Tag+">"
    EndTag = "</"+Tag+">"
    return BeginTag+Txt+EndTag


def make_out_word(out, word):
    BeginTag = out[:2]
    EndTag = out[2:]
    return BeginTag + word + EndTag

def first_last6(nums):
    print(nums)
    if 6 in (nums[0], nums[-1]): return True
    else: return False



def common_end(a,b):
    if (a[0] == b[0]) and (a[-1] == b[-1]): return True
    else: return False




print(common_end([1,2,3], [1,2,]))








