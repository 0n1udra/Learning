
import math
from time import time, sleep
#import time

# 1). Find the sum of all the multiples of 3 or 5 below 1000.
def problem1(Range, n1, n2=0):
    nums = [x for x in range(Range) if (x % n1 == 0 or x % n2 == 0)]
    # if n1 or n2 % == 0 then add to nums
    print(nums)
    print("Sum: ", sum(nums))

    #problem1(1000, 3, 5) > 233168

# By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.
def problem2(Range):
    nums = [1, 2]
    while(True):
        nums.append((nums[-1] + nums[-2]))
        if(nums[-1] > Range): break

    evenFib = [x for x in nums if(x % 2 == 0)]
    print("Fibonacci: ", nums)
    print("Even Fibonacci: ", evenFib)
    print("Sum Even Fibonacci: ", sum(evenFib))
    # problem2(4_000_000)


# Find the largest palindrome made from the product of two 3-digit numbers.
def problem3(Range):
        """prints list of all prime factors for int > 4"""
        n = Range
        L = []

        test = True
        b = n
        while(test):
                i = 2
                while( (b % i != 0 ) & ( i < (b/2))): #find next prime
                        i = i + 1
                if i >= (b/2): #number is prime
                        L.append(b); L.append(1)
                        test = False
                else: #number is not prime
                        a = (b/i)
                        L.append(i)
                        b = a

        return sorted(L)
# print(problem3(600851475143))

# What is the largest prime factor of the number 600851475143 ?
# easier understand version
def problem4(n1, n2):
    def intRev(num): return int(str(num)[::-1])
    # converts to string, then reverses, then converts back to int. does not have any error exception (rn)
    nums = []
    for i in range(n1):
        for y in range(n2):
            x = i * y
            if(x == intRev(x) and x != 0):
                if(x not in nums):
                    nums.append(x)
    nums = sorted(nums, reverse=True)  # reverse sort, shows biggest first
    return nums
    # problem4(999,990)
# more condense, cus y not (not faster)
def problem4_2(n1, n2):
    def intRev(num): return int(str(num)[::-1])
    x = {(x * i) for i in range(n1) for x in range(n2) if((x*i == intRev(i*x)) and (i*x != 0) )}
    return sorted(x, reverse=True)  # so it shows largest number first
# one-liner for no reason, basically no, although most of the times it's .03-0.08 faster (for 999 - 999 range)
def problem4_3(n1, n2, nx1, nx2): return sorted({(x * i) for i in range(n1, n2) for x in range(nx1, nx2) if(x*i == int(str(x*i)[::-1]) and i*x!=0)}, reverse=True)
#print(problem4_3(1000,9999, 1000,9999))

# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
def problem5_1(n1, n2, amount):
    works = []
    x = 1
    while(True):  # infinite loop rn
        for i in range(n1, n2):
            if(x % i != 0): break
            elif(i == n2-1):
                works.append(x)
                print(works)
        x += 1
        if(len(works) >= amount):
            print(works)
            break
#problem5(1, 21, 10)
# my code. SUPER SLOW. SUPER SHITTY. SHIT BRUTE FORCE ATTEMPT

def problem5_2(n):
    t1 = time()

    def gcd(x, y):
        """Find greatest common denominator."""
        while y:
            x, y = y, x % y
        return x

    def gcd_list(lst):
        """Find gcd for any number of integers."""
        res = lst[0]
        for i in lst[1:]:
            res = gcd(res, i)
        return res

    def lcm(x, y):
        """Find lowest common multiple."""
        return int((x * y) / gcd(x, y))

    def lcm_list(lst):
        """Find lcm for any number of integers."""
        res = lst[0]
        for i in lst[1:]:
            res = lcm(res, i)
        return res

    "Computes lowest common multiple for integers from 1 to n."
    print(lcm_list(range(1, n + 1)))
    print(time() - t1)
    # range 1-216

def problem5_3(n1, n2, _ans=1):
    for i in range(n1 ,n2): _ans *= i // math.gcd(i, _ans);
    return str(_ans)
# fastest and simplest so far

# Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
def problem6(n1): print("Difference: ", sum(i for i in range(n1))**2 - sum(y**2 for y in range(n1)))
#problem6(101)

# What is the 10 001st prime number?
def problem7(n):
    # initial prime number list
    prime_list = [2]
    # first number to test if prime
    num = 3
    # keep generating primes until we get to the nth one
    while len(prime_list) < n:

        # check if num is divisible by any prime before it
        for p in prime_list:
            # if there is no remainder dividing the number
            # then the number is not a prime
            if num % p == 0:
                # break to stop testing more numbers, we know it's not a prime
                break

        # if it is a prime, then add it to the list
        # after a for loop, else runs if the "break" command has not been given
        else:
            # append to prime list
            prime_list.append(num)

        # same optimization you had, don't check even numbers
        num += 2

    # return the last prime number generated
    return prime_list[-1]
# This code is contributed by Sachin Bisht
#print(problem7(10001))


def problem9():
    num = '\
    73167176531330624919225119674426574742355349194934\
    96983520312774506326239578318016984801869478851843\
    85861560789112949495459501737958331952853208805511\
    12540698747158523863050715693290963295227443043557\
    66896648950445244523161731856403098711121722383113\
    62229893423380308135336276614282806444486645238749\
    30358907296290491560440772390713810515859307960866\
    70172427121883998797908792274921901699720888093776\
    65727333001053367881220235421809751254540594752243\
    52584907711670556013604839586446706324415722155397\
    53697817977846174064955149290862569321978468622482\
    83972241375657056057490261407972968652414535100474\
    82166370484403199890008895243450658541227588666881\
    16427171479924442928230863465674813919123162824586\
    17866458359124566529476545682848912883142607690042\
    24219022671055626321111109370544217506941658960408\
    07198403850962455444362981230987879927244284909188\
    84580156166097919133875499200524063689912560717606\
    05886116467109405077541002256983155200055935729725\
    71636269561882670428252483600823257530420752963450'

    biggest = 0
    i = 0
    while i < len(num) - 4:
        one = int(num[i])
        two = int(num[i + 1])
        thr = int(num[i + 2])
        fou = int(num[i + 3])
        fiv = int(num[i + 4])
        product = one * two * thr * fou * fiv
        if product > biggest:
            biggest = product
        i = i + 1
    print(biggest)

    print("This code took: " + str(elapsed) + " seconds")








